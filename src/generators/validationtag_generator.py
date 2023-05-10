from faker import Faker
import src.dependencies.models.validation_tag as validation_tag_models


class ValidationTagSampleGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate(self):
        validation_tag_name = self.fake.random_element(elements=("Signature", "IFG", "Packet Fields", "GPTP", "IET", "Bundle", "AFDX", "Session APIs")) + ' Validation'
        return validation_tag_models.ValidationTagModel(
            name=validation_tag_name,
            metaData={
                "Description": f"{validation_tag_name} is enabled ",
                "Executable Path": f"/analyzers/analyzers_exec/ve_{validation_tag_name.replace(' ', '').lower()}.o",
            }
        )
