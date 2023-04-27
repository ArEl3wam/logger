import json
from collections import OrderedDict

from validation_tag import ValidationTag
import result


class TestCase:
    def __init__(self, meta_data: dict, parent_ts):
        self.meta_data = meta_data
        self.parent_ts = parent_ts
        self.validation_tags = []

        self.db_id = None
        self.is_success = False

    def create_validation_tag(self, name: str, meta_data: dict):
        validation_tag_obj = ValidationTag(
            name=name,
            meta_data=meta_data,
            parent_tc=self,
            parent_ts=self.parent_ts
        )
        self.validation_tags.append(validation_tag_obj)
        return validation_tag_obj

    def push_to_db(self):
        # set db_id
        for validation_tag_obj in self.validation_tags:
            validation_tag_obj.push_to_db()

    def get_db_id(self):
        if self.db_id is None:
            self.push_to_db()
        return self.db_id

    def dict(self):
        return {
            "meta_data": self.meta_data,
            "validation_tags": self.generate_validation_tags()
        }

    def generate_validation_tags(self):
        return [validation_tag_obj.dict() for validation_tag_obj in self.validation_tags]


if __name__ == "__main__":
    tc = TestCase(
        meta_data={
            "description": "Packet Fields Validation"
        },
        parent_ts=None
    )
    vt = tc.create_validation_tag(
        name="Packet Fields Elements Validation",
        meta_data={
            "description": "Packet Fields Elements Validation"
        }
    )
    vp = vt.create_validation_point(
        levels=OrderedDict(
            mac=1,
            phy=2,
            fec=3
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
    vp.add_result(
        result.Result(
            name="Packet Fields Elements Validation",
            result_info=result.ResultInfo(
                actual=[1, 2, 3],
                expected=[1, 2, 3],
                tolerance=0.1,
                status="pass"
            )
        )
    )
    print(json.dumps(tc.dict(), indent=2))

