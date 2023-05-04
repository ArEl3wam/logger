from src.dependencies.utils.requests_handler import RequestsHandler


class ValidationPoint:
    def __init__(self, validation_point_model, test_suite_ref, validation_tag_ref, test_case_ref):
        self.meta_data = validation_point_model
        self.parent_test_suite = test_suite_ref
        self.parent_test_case = test_case_ref
        self.parent_validation_tag = validation_tag_ref

        self.db_id = None
        self.is_success = False
        self.url_postfix = "/TestSuite/{test_suite_id}/TestCase/{test_case_id}/ValidationTag/{validation_tag_id}/ValidationPoint"

        self.requests_handler = RequestsHandler.get_instance()

    def json(self):
        d = self.meta_data.dict()
        d.update({"isSuccessful": self.is_success})
        return d

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
            print(self.url_postfix)
            self.db_id = self.requests_handler.push(self.url_postfix, self.json())

    def push_all(self):
        self.push()
