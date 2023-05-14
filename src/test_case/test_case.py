from datetime import datetime

import src.dependencies.models.validation_tag as validation_tag_models
from src.dependencies.models.test_case import TestCaseModel
from src.dependencies.utils.requests_handler import RequestsHandler
from src.validation_tag.validation_tag import ValidationTag


class TestCase:
    def __init__(self, test_case_model: TestCaseModel, test_suite_ref):
        self.meta_data = test_case_model.dict()
        self.parent_test_suite = test_suite_ref
        self.validation_tags = []

        self.db_id = None
        self.is_success = True
        self.creation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.url_postfix = "testSuite/{test_suite_id}/testCases/"
        self.requests_handler = RequestsHandler.get_instance()

    def create_validation_tag(self, validation_tag_model: validation_tag_models.ValidationTagModel):
        vt = ValidationTag(validation_tag_model, self.parent_test_suite, self)
        self.validation_tags.append(vt)
        return vt

    def update_status(self, is_success: bool):
        if not self.is_success:
            return
        if self.is_success and is_success:
            return

        self.is_success = is_success
        url_postfix = "testCases/{test_case_id}".format(test_case_id=self.db_id)
        self.requests_handler.patch(url_postfix, {"isSuccessful": self.is_success})
        self.parent_test_suite.update_status(is_success)

    def json(self):
        return {"metaData": self.meta_data, "isSuccessful": self.is_success, "creationDate": self.creation_date}

    def push(self):
        if not self.db_id:
            self.parent_test_suite.push()
            self.db_id = self.requests_handler.push(
                self.url_postfix.format(test_suite_id=self.parent_test_suite.db_id), self.json()
            )

    def push_all(self):
        self.push()
        for vt in self.validation_tags:
            vt.push_all()
