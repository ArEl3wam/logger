from pydantic import BaseModel


class StandAloneAttributes(BaseModel):
    id: int
    mii_enum: str
    miiLaneNumber: int
    miiLaneWidth: int
    miiSpeed: int
    compiledFEC: str
    miiWireDelay: int


class MPGAttributes(BaseModel):
    id: int
    compiledFEC: str
    mpgPortIdOffset: int
    mpgPortsNumber: int
    mpgLanesNumber: int
    mpgMaxLanesNumberList: int
    mpgLaneWidth: int
    mpgMaxLaneWidthList: int
    mpgOneG_ENABLED: int
    mpgWireDelay: int


class DUTInstanceInfo(BaseModel):
    sa_configuration: list[StandAloneAttributes]
    mpg_configuration: list[MPGAttributes]


class DUTConnectivityMap(BaseModel):
    sa_connectivity_map: dict[str, str]
    mpg_connectivity_map: dict[str, str]


class DesignInfo(BaseModel):
    dut_instance_info: DUTInstanceInfo
    dut_connectivity_map: DUTConnectivityMap


class TestSuiteModel(BaseModel):
    owner: str
    version: str
    machine: str
    running_mode: str
    platform: str
    solution: str
    tool_name: str
    metaData: str
    date: str
    design_info: DesignInfo
