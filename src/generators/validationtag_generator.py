from faker import Faker
import src.dependencies.models.validation_tag as validation_tag_models


class ValidationTagSampleGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate(self):
        return validation_tag_models.ValidationTagModel(
            name=self.fake.name(),
            metaData={
                "description": self.fake.text(),
                "executable_path": self.fake.file_path(),
            }
        )
