import json
from collections import OrderedDict

import test_case
from src import result


class TestSuite:
    def __init__(self, meta_data: dict):
        self.meta_data = meta_data
        self.test_cases = []
        self.validation_tags = []

        self.db_id = None
        self.is_success = False

    def create_test_case(self, meta_data: dict):
        test_case_obj = test_case.TestCase(
            meta_data=meta_data,
            parent_ts=self
        )
        self.test_cases.append(test_case_obj)
        return test_case_obj

    def create_validation_tag(self, name: str, meta_data: dict):
        validation_tag_obj = test_case.ValidationTag(
            name=name,
            meta_data=meta_data,
            parent_ts=self
        )
        self.validation_tags.append(validation_tag_obj)
        return validation_tag_obj

    def push_to_db(self):
        # set db_id
        for test_case_obj in self.test_cases:
            test_case_obj.push_to_db()
        for validation_tag_obj in self.validation_tags:
            validation_tag_obj.push_to_db()

    def get_db_id(self):
        if self.db_id is None:
            self.push_to_db()
        return self.db_id

    def dict(self):
        return {
            "meta_data": self.meta_data,
            "test_cases": self.generate_test_cases(),
            "validation_tags": self.generate_validation_tags()
        }

    def generate_test_cases(self):
        return [test_case_obj.dict() for test_case_obj in self.test_cases]

    def generate_validation_tags(self):
        return [validation_tag_obj.dict() for validation_tag_obj in self.validation_tags]


if __name__ == "__main__":
    ts = TestSuite(
        meta_data={
            "description": "Packet Fields Validation",
            "author": "Saurabh"
        }
    )
    tc = ts.create_test_case(
        meta_data={
            "description": "Packet Fields Elements Validation"
        }
    )
    vt = tc.create_validation_tag(
        name="Packet Fields Elements Validation",
        meta_data={
            "description": "Packet Fields Elements Validation"
        }
    )
    vp = vt.create_validation_point(
        levels=OrderedDict(
            mac=2
        ),
        meta_data={
            "description": "Packet Fields Elements Validation"
        }
    )
    vp.add_result(
        result.Result(
            name="Packet Fields Elements Validation",
            result_info=result.ResultInfo(
                actual=1,
                expected=1,
                tolerance=0.1,
                status="pass"
            )
        )
    )
    print(json.dumps(ts.dict(), indent=4))
