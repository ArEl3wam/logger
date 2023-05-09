from src.dependencies.models.validation_point import ValidationPointModel
from src.validation_point.validation_point import ValidationPoint
from src.dependencies.utils.requests_handler import RequestsHandler


class ValidationTag:
    def __init__(self, validation_tag_model, test_suite_ref, test_case_ref=None):
        self.meta_data = validation_tag_model
        self.parent_test_suite = test_suite_ref
        self.parent_test_case = test_case_ref
        self.validation_points = []

        self.db_id = None
        self.is_success = True

        if test_case_ref:
            self.url_postfix = "validationTags/testSuites/{test_suite_id}/testCases/{test_case_id}"
        else:
            self.url_postfix = "validationTags/testSuites/{test_suite_id}"

        self.requests_handler = RequestsHandler.get_instance()

    def create_validation_point(self, validation_point_model: ValidationPointModel):
        vp = ValidationPoint(validation_point_model, self.parent_test_suite, self, self.parent_test_case)
        self.validation_points.append(vp)
        return vp

    def update_status(self, is_success: bool):
        if not self.is_success:
            return  # if validation tag is already failed, it cannot be successful again
        if self.is_success and is_success:
            return  # if validation tag is already successful, and it is successful again, do nothing

        self.is_success = is_success  # if validation tag is successful, and it is failed now, update state
        url_postfix = "validationTags/{validation_tag_id}".format(validation_tag_id=self.db_id)
        self.requests_handler.patch(url_postfix, {"isSuccessful": self.is_success})
        self.parent_test_case.update_status(is_success)

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
