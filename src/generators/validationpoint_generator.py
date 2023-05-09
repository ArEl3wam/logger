from faker import Faker
from src.dependencies.models.validation_point import ValidationPointModel


class ValidationPointSampleGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate(self):
        levels = [
            {
                self.fake.word(): self.fake.word()
            } for _ in range(3)
        ]
        meta_data = {
            self.fake.word(): self.fake.word()
            for _ in range(self.fake.random_int(min=1, max=5))
        }
        return ValidationPointModel(
            levels=levels,
            meta_data=meta_data
        )

    def generate_result(self):
        return {
            "name": self.fake.word(),
            "actual": self.fake.word(),
            "expected": self.fake.word(),
            "tolerance": self.fake.random_int(min=0, max=100),
        }
