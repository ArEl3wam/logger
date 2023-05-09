from faker import Faker
import src.dependencies.models.test_suite as test_suite_models


class TestSuiteSampleGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate(self):
        fake = self.fake
        # generate random StandAloneAttributes objects
        sa_configuration = []
        for i in range(fake.random_int(min=1, max=5)):
            sa_configuration.append(
                test_suite_models.StandAloneAttributes(
                    id=i + 1,
                    mii_enum=fake.random_element(elements=("GMII", "XGMII")),
                    miiLaneNumber=fake.random_int(min=1, max=4),
                    miiLaneWidth=fake.random_int(min=32, max=128, step=32),
                    miiSpeed=fake.random_int(min=1, max=100),
                    compiledFEC=fake.random_element(elements=("NO_FEC", "RS_FEC")),
                    miiWireDelay=fake.random_int(min=0, max=5000),
                )
            )

        # generate random MPGAttributes objects
        mpg_configuration = []
        for i in range(fake.random_int(min=1, max=5)):
            mpg_configuration.append(
                test_suite_models.MPGAttributes(
                    id=i + 1,
                    compiledFEC=fake.random_element(elements=("NO_FEC", "RS_FEC")),
                    mpgPortIdOffset=fake.random_int(min=0, max=4),
                    mpgPortsNumber=fake.random_int(min=1, max=8),
                    mpgLanesNumber=fake.random_int(min=1, max=4),
                    mpgMaxLanesNumberList=fake.random_int(min=1, max=4),
                    mpgLaneWidth=fake.random_int(min=32, max=128, step=32),
                    mpgMaxLaneWidthList=fake.random_int(min=32, max=128, step=32),
                    mpgOneG_ENABLED=fake.random_int(min=0, max=1),
                    mpgWireDelay=fake.random_int(min=0, max=5000),
                )
            )

        # generate random sa_connectivity_map and mpg_connectivity_map dictionaries
        sa_connectivity_map = {str(i + 1): str(fake.random_int(min=1, max=2)) for i in range(fake.random_int(min=1, max=6))}
        mpg_connectivity_map = {str(i + 1): str(fake.random_int(min=1, max=2)) for i in range(fake.random_int(min=1, max=6))}

        # initialize the DUTInstanceInfo, DUTConnectivityMap, and DesignInfo objects with the generated data
        dut_instance_info = test_suite_models.DUTInstanceInfo(sa_configuration=sa_configuration,
                                                              mpg_configuration=mpg_configuration)
        dut_connectivity_map = test_suite_models.DUTConnectivityMap(sa_connectivity_map=sa_connectivity_map,
                                                                    mpg_connectivity_map=mpg_connectivity_map)
        design_info = test_suite_models.DesignInfo(dut_instance_info=dut_instance_info,
                                                   dut_connectivity_map=dut_connectivity_map)

        # generate a TestSuite object with the generated data
        return test_suite_models.TestSuiteModel(
                owner=fake.name(),
                version=fake.random_int(),
                machine=fake.word(),
                running_mode=fake.word(),
                platform=fake.word(),
                solution=fake.word(),
                tool_name=fake.word(),
                metaData=fake.sentence(),
                date=str(fake.date_time()),
                design_info=design_info,
        )
