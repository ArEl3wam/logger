from src.dependencies.models.test_suite import TestSuiteModel
from src.dependencies.models.test_case import TestCaseModel
from src.dependencies.models.validation_tag import ValidationTagModel
from src.dependencies.utils.requests_handler import RequestsHandler

import src.test_case.test_case as test_case
from src.validation_tag.validation_tag import ValidationTag


class TestSuite:
    def __init__(self, test_suite_model: TestSuiteModel):
        self.meta_data = test_suite_model
        self.test_cases: list[test_case.TestCase] = []
        self.validation_tags = []

        self.db_id = None
        self.is_success = False
        self.url_postfix = "TestSuites/"
        self.requests_handler = RequestsHandler.get_instance()

    def create_test_case(self, test_case_model: TestCaseModel):
        tc = test_case.TestCase(test_case_model, self)
        self.test_cases.append(tc)
        return tc

    def create_validation_tag(self, validation_tag_model: ValidationTagModel):
        vt = ValidationTag(validation_tag_model, self)
        self.validation_tags.append(vt)
        return vt

    def json(self):
        return {"metaData": self.meta_data.dict(), "isSuccessful": self.is_success}

    def push(self):
        if not self.db_id:
            self.db_id = self.requests_handler.push(self.url_postfix, self.json())

    def push_all(self):
        self.push()
        for tc in self.test_cases:
            tc.push_all()
