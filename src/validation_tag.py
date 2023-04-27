from collections import OrderedDict

from src import result
from src.validation_point import ValidationPoint


class ValidationTag:
    def __init__(
            self,
            name: str,
            meta_data: dict,
            parent_ts,
            parent_tc=None
    ):
        self.name = name
        self.meta_data = meta_data
        self.validation_points = []

        self.parent_ts = parent_ts
        self.parent_tc = parent_tc

        self.db_id = None
        self.is_success = False

    def create_validation_point(self, levels: OrderedDict, meta_data: dict):
        validation_point_obj = ValidationPoint(
            parent_vt=self,
            levels=levels,
            meta_data=meta_data
        )
        self.validation_points.append(validation_point_obj)
        return validation_point_obj

    def push_to_db(self):
        # set db_id
        for validation_point_obj in self.validation_points:
            validation_point_obj.push_to_db()

    def get_db_id(self):
        if self.db_id is None:
            self.push_to_db()
        return self.db_id

    def dict(self):
        return {
            "name": self.name,
            "meta_data": self.meta_data,
            "validation_points": self.generate_validation_points()
        }

    def generate_validation_points(self):
        return [validation_point_obj.dict() for validation_point_obj in self.validation_points]


if __name__ == "__main__":
    import json

    vt = ValidationTag(
        name="Packet Fields Elements Validation",
        meta_data={
            "description": "Validating Packet Fields Element for each Mac in Rx and Tx Direction",
            "executable_path": "/project/path/to/executable"
        },
        parent_ts=None,
    )
    vp1 = vt.create_validation_point(
        levels=OrderedDict(
            mac=1,
            direction="Rx",
            packet_field="Dst Mac Address"
        ),
        meta_data={
            "description": "Validating Dst Mac Address for Mac 1 in Rx Direction",
            "executable_path": "/project/path/to/executable"
        }
    )
    vp1.add_result(
        result.Result(
            name="flow_number_152",
            result_info=result.ResultInfo(
                expected=0,
                actual=1,
                tolerance=0,
                status="fail"
            )
        )
    )
    vp1.add_result(
        result.Result(
            name="flow_number_153",
            result_info=result.ResultInfo(
                expected=0,
                actual=0,
                tolerance=0,
                status="pass"
            )
        )
    )
    vp2 = vt.create_validation_point(
        levels=OrderedDict(
            mac=1,
            direction="Tx",
            packet_field="Packet Length"
        ),
        meta_data={
            "description": "Validating Packet Length for Mac 1 in Tx Direction",
            "executable_path": "/project/path/to/executable"
        }
    )
    vp2.add_result(
        result.Result(
            name="flow_number_152",
            result_info=result.ResultInfo(
                expected=0,
                actual=0,
                tolerance=0,
                status="pass"
            )
        )
    )
    vp2.add_result(
        result.Result(
            name="flow_number_153",
            result_info=result.ResultInfo(
                expected=0,
                actual=0,
                tolerance=0,
                status="pass"
            )
        )
    )
    vp3 = vt.create_validation_point(
        levels=OrderedDict(
            mac=1,
            direction="Rx",
            packet_field="Dst Mac Address"
        ),
        meta_data={
            "description": "Validating Dst Mac Address for Mac 1 in Rx Direction",
            "executable_path": "/project/path/to/executable"
        }
    )
    vp3.add_result(
        result.Result(
            name="flow_number_152",
            result_info=result.ResultInfo(
                expected=0,
                actual=1,
                tolerance=0,
                status="fail"
            )
        )
    )
    vp3.add_result(
        result.Result(
            name="flow_number_153",
            result_info=result.ResultInfo(
                expected=0,
                actual=0,
                tolerance=0,
                status="pass"
            )
        )
    )
    vp4 = vt.create_validation_point(
        levels=OrderedDict(
            mac=2,
            direction="Tx",
            packet_field="Packet Length"
        ),
        meta_data={
            "description": "Validating Packet Length for Mac 2 in Tx Direction",
            "executable_path": "/project/path/to/executable"
        }
    )
    vp4.add_result(
        result.Result(
            name="flow_number_25",
            result_info=result.ResultInfo(
                expected=1000,
                actual=1000,
                tolerance=0,
                status="pass"
            )
        )
    )
    vp4.add_result(
        result.Result(
            name="flow_number_26",
            result_info=result.ResultInfo(
                expected=1000,
                actual=1000,
                tolerance=0,
                status="pass"
            )
        )
    )
    print(json.dump(vt.dict(), open("test.json", "w"), indent=2))

























