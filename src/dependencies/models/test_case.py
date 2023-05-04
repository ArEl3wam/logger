from pydantic import BaseModel


class RunningMacsInfo(BaseModel):
    id: int
    mii_type: str


class DUTMasterSlaveInfo(BaseModel):
    master_id: int
    slave_ids: list[int]


class MacsConfiguration(BaseModel):
    streaming_type_configuration: dict[str, str]
    wire_delay_configuration: dict[str, str]
    gptp_configuration: dict[str, str]
    afdx_configuration: dict[str, str]
    addresses_configuration: dict[str, str]


class MpgConfiguration(BaseModel):
    ports_configuration: list[dict[str, str]]
    fec_configuration: dict[str, str]


class TestCaseModel(BaseModel):
    macs_info: list[RunningMacsInfo]
    dut_master_slave_info: list[DUTMasterSlaveInfo]
    macs_configuration: dict[int, MacsConfiguration]
    mpg_configuration: dict[int, MpgConfiguration]
