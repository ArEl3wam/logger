from faker import Faker
import src.dependencies.models.test_suite as test_suite_models


class TestSuiteSampleGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate(self):
        fake = self.fake
        sa_configuration = []
        for i in range(fake.random_int(min=1, max=5)):
            sa_configuration.append(
                test_suite_models.StandAloneAttributes(
                    id=i + 1,
                    mii_enum=fake.random_element(elements=("GMII", "XGMII", "CGMII", "25GMII")),
                    miiLaneNumber=fake.random_element(elements=(1, 4, 16)),
                    miiLaneWidth=fake.random_element(elements=(32, 64, 128, 256)),
                    miiSpeed=fake.random_element(elements=(1, 10, 25, 100)),
                    compiledFEC=fake.random_element(elements=("NO_FEC", "RS_FEC", "FC_FEC", "RS_FC_FEC")),
                    miiWireDelay=fake.random_int(min=0, max=5000),
                )
            )

        mpg_configuration = []
        for i in range(fake.random_int(min=1, max=5)):
            mpg_configuration.append(
                test_suite_models.MPGAttributes(
                    id=i + 1,
                    compiledFEC=fake.random_element(elements=("NO_FEC", "RS_FEC", "FC_FEC", "RS_FC_FEC")),
                    mpgPortIdOffset=fake.random_int(min=0, max=20),
                    mpgPortsNumber=fake.random_element(elements=(1, 4, 8, 16)),
                    mpgLanesNumber=fake.random_element(elements=(1, 4, 8, 16)),
                    mpgMaxLanesNumberList=fake.random_element(elements=(1, 4, 8, 16, 64)),
                    mpgLaneWidth=fake.random_int(min=32, max=128, step=32),
                    mpgMaxLaneWidthList=fake.random_int(min=32, max=128, step=32),
                    mpgOneG_ENABLED=fake.random_int(min=0, max=1),
                    mpgWireDelay=fake.random_int(min=0, max=5000),
                )
            )

        # generate random sa_connectivity_map and mpg_connectivity_map dictionaries
        sa_connectivity_map = {}
        mpg_connectivity_map = {}
        idx = 1
        for i in range(fake.random_int(min=1, max=6)):
            is_loopback_sa_co_mpg = fake.boolean()
            if is_loopback_sa_co_mpg:
                sa_connectivity_map[str(idx)] = str(idx)
                mpg_connectivity_map[str(idx)] = str(idx + 1)
                mpg_connectivity_map[str(idx + 1)] = str(idx)
                idx += 1
            else:
                sa_connectivity_map[str(idx)] = str(idx + 1)
                sa_connectivity_map[str(idx + 1)] = str(idx)
                mpg_connectivity_map[str(idx)] = str(idx)
                idx += 1
            idx += 1

        # initialize the DUTInstanceInfo, DUTConnectivityMap, and DesignInfo objects with the generated data
        dut_instance_info = test_suite_models.DUTInstanceInfo(
            sa_configuration=sa_configuration,
            mpg_configuration=mpg_configuration
        )
        dut_connectivity_map = test_suite_models.DUTConnectivityMap(
            sa_connectivity_map=sa_connectivity_map,
            mpg_connectivity_map=mpg_connectivity_map
        )
        design_info = test_suite_models.DesignInfo(
            dut_instance_info=dut_instance_info,
            dut_connectivity_map=dut_connectivity_map
        )

        # generate a TestSuite object with the generated data
        return test_suite_models.TestSuiteModel(
            owner=fake.random_element(elements=("Mustafa El-Antrawy", "Ahmed Seif", "Ola Alaa", "Noha Gamal", "Merna Ashraf", "Mahmoud Sabra")),
            version=f"{fake.random_int(min=11, max=12)}.{fake.random_int(min=1, max=8)}.{fake.random_int(min=1, max=3)}",
            machine=fake.random_element(elements=("egc-med-einstein", "egc-med-nmahfouz", "egc-med-berners", "egc-med-edison")),
            compilation_mode=fake.random_element(elements=("Emulation", "Simulation", "Velclkgen", "Hybrid")),
            platform=fake.random_element(elements=("Veloce", "VPS")),
            solution="Ethernet",
            tool_name=fake.random_element(elements=("EPGM", "Controller")),
            metaData=fake.random_element(elements=("GPTP Feature Testing", "AFDX Feature Testing", "System Testing", "Official Release")),
            design_info=design_info,
        )
