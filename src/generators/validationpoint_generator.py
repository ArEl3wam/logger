from faker import Faker
from src.dependencies.models.validation_point import ValidationPointModel


class ValidationPointSampleGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate(self):
        levels = [{"mac": self.fake.random_int(min=1, max=64)},
                  {"direction": self.fake.random_element(elements=("Rx", "Tx"))}]

        meta_data = {
            "Additional Info": "No Additional Info supplied"
        }
        return ValidationPointModel(
            levels=levels,
            meta_data=meta_data
        )

    def generate_result(self, status: str):
        name = self.fake.random_element(elements=("Packets Parsed", "Total Flows", "Signatured Packets", "Errors Count"))
        tolerance = self.fake.random_int(min=0, max=1)
        if status == "fail":
            return {
                "name": name,
                "actual": self.fake.random_element(elements=(100, 105, 110)),
                "expected": self.fake.random_element(elements=(101, 106, 1210)),
                "tolerance": tolerance
            }
        else:
            element = self.fake.random_element(elements=(100, 105, 110))
            return {
                "name": name,
                "actual": element,
                "expected": element,
                "tolerance": tolerance
            }
