from faker import Faker
import src.dependencies.models.test_case as test_case_models


class TestCaseSampleGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate(self):
        fake = self.fake

        running_macs_info = [
            test_case_models.RunningMacsInfo(
                id=fake.random_int(min=1, max=64),
                mii_type=fake.word()
            )
            for _ in range(3)
        ]

        dut_master_slave_info = []
        for i in range(3):
            master_id = fake.random_int(min=1, max=64)
            slave_ids = [
                fake.random_int(min=1, max=64)
                for _ in range(fake.random_int(min=1, max=3))
            ]
            dut_master_slave_info.append(
                test_case_models.DUTMasterSlaveInfo(master_id=master_id, slave_ids=slave_ids)
            )

        # Generate fake MacsConfiguration objects
        macs_configuration = {}
        for i in range(3):
            mac_id = fake.random_int(min=1, max=64)
            macs_configuration[mac_id] = test_case_models.MacsConfiguration(
                streaming_type_configuration={
                    "Streaming Type": fake.random_element(elements=("Packet", "Bundle", "GPTP", "IET")),
                    "Packets Per Burst": fake.random_int(1, 100)
                },
                wire_delay_configuration={
                    "Enable": fake.boolean(),
                    "Value": fake.random_int(1, 3000)
                },
                gptp_configuration={
                    "Enable": fake.boolean()
                },
                afdx_configuration={
                    "Packet Identifier": fake.hexify(text="^^^^^^^^^^^"),
                    "Error Injection": fake.boolean()},
                addresses_configuration={
                    "Mode": fake.random_element(elements=("Static", "Sweep", "Random"))
                }
            )

        # Generate fake MpgConfiguration objects
        mpg_configuration = {}
        for i in range(3):
            mpg_id = fake.random_int(min=1, max=100)
            mpg_configuration[mpg_id] = test_case_models.MpgConfiguration(
                ports_configuration=[
                    {
                        "Port Offset": str(fake.random_int(min=1, max=10)),
                        "Port Type": fake.word()
                    }
                    for _ in range(fake.random_int(min=1, max=2))
                ],
                fec_configuration={
                    "Enable": fake.boolean()
                }
            )

        # Generate fake TestCaseModel object
        return test_case_models.TestCaseModel(
            macs_info=running_macs_info,
            dut_master_slave_info=dut_master_slave_info,
            macs_configuration=macs_configuration,
            mpg_configuration=mpg_configuration
        )
