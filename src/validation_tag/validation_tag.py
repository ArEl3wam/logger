from src.validation_point.validation_point import ValidationPoint
from src.dependencies.utils.requests_handler import RequestsHandler


class ValidationTag:
    def __init__(self, validation_tag_model, test_suite_ref, test_case_ref=None):
        self.meta_data = validation_tag_model
        self.parent_test_suite = test_suite_ref
        self.parent_test_case = test_case_ref
        self.validation_points = []

        self.db_id = None
        self.is_success = False

        if test_case_ref:
            self.url_postfix = "validationTags/testSuites/{test_suite_id}/testCases/{test_case_id}"
        else:
            self.url_postfix = "validationTags/testSuites/{test_suite_id}"

        self.requests_handler = RequestsHandler.get_instance()

    def create_validation_point(self, validation_point_model):
        vp = ValidationPoint(validation_point_model, self.parent_test_suite, self, self.parent_test_case)
        self.validation_points.append(vp)
        return vp

    def json(self):
        return {"metaData": self.meta_data.dict(), "isSuccessful": self.is_success}

    def push(self):
        if not self.db_id:
            self.parent_test_suite.push()
            if self.parent_test_case:
                self.parent_test_case.push()
                self.url_postfix = self.url_postfix.format(
                    test_suite_id=self.parent_test_suite.db_id,
                    test_case_id=self.parent_test_case.db_id
                )
            else:
                self.url_postfix = self.url_postfix.format(
                    test_suite_id=self.parent_test_suite.db_id
                )
            self.db_id = self.requests_handler.push(self.url_postfix, self.json())

    def push_all(self):
        self.push()
        for vp in self.validation_points:
            vp.push_all()
