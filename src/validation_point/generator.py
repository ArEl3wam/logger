from faker import Faker


class ValidationPointSampleGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate(self):
        levels = [
            {self.fake.word(): self.fake.word()} for _ in range(3)
        ]
        meta_data = {
            self.fake.word(): self.fake.word() for _ in range(self.fake.random_int(min=1, max=5))
        }
        return {
            "levels": levels,
            "meta_data": meta_data
        }

    def generate_result(self):
        return {
            "name": self.fake.word(),
            "actual": "please pass",
            "expected": "please pass",
            "tolerance": 0
        }
