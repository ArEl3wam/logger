from collections import OrderedDict

from src import result, resultinfo


class ValidationPoint:
    def __init__(
            self,
            levels: OrderedDict,
            meta_data: dict,
            parent_vt
    ):
        self.parent_vt = parent_vt

        self.levels = levels
        self.meta_data = meta_data
        self.results = []

        self.db_id = None
        self.is_success = False

    def add_result(self, result_obj: result.Result):
        self.results.append(result_obj)

    def push_to_db(self):
        parent_db_id = self.parent_vt.get_db_id()
        # make an http request and get the id of this vp from response

    def dict(self):
        return {
            "levels": self.generate_levels(),
            "meta_data": self.meta_data,
            "results": self.generate_results()
        }

    def generate_levels(self):
        return [{key: value} for key, value in self.levels.items()]

    def generate_results(self):
        return {result_obj.name: result_obj.result_info.dict() for result_obj in self.results}


if __name__ == "__main__":
    import json

    levels = OrderedDict()
    meta_data = {
        "description": "Validation Signature Settings"
    }
    flow_number_size = result.Result(
        name="flow_number_size",
        result_info=resultinfo.ResultInfo(
            actual=2,
            expected=2,
            tolerance=0,
            status="pass"
        )
    )
    sequence_number_size = result.Result(
        name="sequence_number_size",
        result_info=resultinfo.ResultInfo(
            actual=4,
            expected=5,
            tolerance=0,
            status="fail"
        )
    )
    validation_point = ValidationPoint(levels=levels, meta_data=meta_data, parent_vt=None)
    validation_point.add_result(flow_number_size)
    validation_point.add_result(sequence_number_size)
    print(json.dumps(validation_point.dict(), indent=4))

    levels = OrderedDict()
    levels["mac"] = 1
    meta_data = {
        "description": "Validation FEC for Mac 1",
        "mac_mii_type": "CGMII-PCS-4x40"
    }
    fec_errors = result.Result(
        name="fec_errors",
        result_info=resultinfo.ResultInfo(
            actual="RC",
            expected="RC",
            status="pass"
        )
    )
    validation_point = ValidationPoint(levels=levels, meta_data=meta_data, parent_vt=None)
    validation_point.add_result(fec_errors)
    print(json.dumps(validation_point.dict(), indent=4))

    levels = OrderedDict()
    levels["mac"] = 1
    levels["direction"] = "tx"
    levels["packet_fields"] = "Dst Mac Address"

    meta_data = {
        "description": "Validation Dst Mac Address for Mac 1",
        "executable_path": "path/to/executable",
    }
    flow_number_152 = result.Result(
        name="flow_number_152",
        result_info=resultinfo.ResultInfo(
            actual=2,
            expected=2,
            tolerance=0,
            status="pass"
        )
    )
    flow_number_153 = result.Result(
        name="flow_number_153",
        result_info=resultinfo.ResultInfo(
            actual=2,
            expected=2,
            tolerance=0,
            status="pass"
        )
    )
    validation_point = ValidationPoint(levels=levels, meta_data=meta_data)
    validation_point.add_result(flow_number_152)
    validation_point.add_result(flow_number_153)
    print(json.dumps(validation_point.dict(), indent=4))
