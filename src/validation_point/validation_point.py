from collections import defaultdict

from src.comparator.comparator import Comparator
from src.dependencies.utils.requests_handler import RequestsHandler
from src.dependencies.models.validation_point import ValidationPointModel


class ValidationPoint:
    def __init__(
            self,
            validation_point_model: ValidationPointModel,
            test_suite_ref,
            validation_tag_ref,
            test_case_ref
    ):
        self.levels = validation_point_model.levels
        self.meta_data = validation_point_model.meta_data
        self.results: dict[str, dict] = defaultdict(dict)
        self.parent_test_suite = test_suite_ref
        self.parent_test_case = test_case_ref
        self.parent_validation_tag = validation_tag_ref

        self.db_id = None
        self.is_success = True
        self.url_postfix = "TestSuite/{test_suite_id}/TestCase/{test_case_id}/" \
                           "ValidationTag/{validation_tag_id}/ValidationPoint"

        self.requests_handler = RequestsHandler.get_instance()

    def create_result(self, name, actual, expected, tolerance=0):
        result = Comparator.compare_dict(
            {
                "actual": actual,
                "expected": expected,
                "tolerance": tolerance
            }
        )
        status = result["status"]
        self.results[f"{name}"] = {
            "actual": actual,
            "expected": expected,
            "tolerance": tolerance,
            "status": status,
        }
        self.update_status(status == "pass")

    def update_status(self, is_success: bool):
        if not self.is_success:
            return
        if self.is_success and is_success:
            return
        self.is_success = is_success
        self.push()
        url_postfix = "validationPoints/{validation_point_id}".format(validation_point_id=self.db_id)
        self.requests_handler.patch(url_postfix, {"isSuccessful": self.is_success})
        self.parent_validation_tag.update_status(is_success)

    def json(self):
        return {
            "levels": self.levels,
            "metaData": self.meta_data,
            "results": self.results,
            "isSuccessful": self.is_success,
        }

    def push(self):
        if not self.db_id:
            self.parent_test_suite.push()
            self.parent_test_case.push()
            self.parent_validation_tag.push()
            self.url_postfix = self.url_postfix.format(
                test_suite_id=self.parent_test_suite.db_id,
                test_case_id=self.parent_test_case.db_id,
                validation_tag_id=self.parent_validation_tag.db_id
            )
            self.db_id = self.requests_handler.push(self.url_postfix, self.json())

    def push_all(self):
        self.push()
