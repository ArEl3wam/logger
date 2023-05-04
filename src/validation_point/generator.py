from faker import Faker

import src.dependencies.models.validation_point as validation_point_models


class ValidationPointSampleGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate(self):
        levels = [
            {self.fake.word(): self.fake.word()} for _ in range(3)
        ]
        metaData = {
            self.fake.word(): self.fake.word() for _ in range(self.fake.random_int(min=1, max=5))
        }
        results = [
            validation_point_models.Result(
                name=self.fake.word(),
                result_info=validation_point_models.ResultInfo(
                    actual=self.fake.word(),
                    expected=self.fake.word(),
                    tolerance=self.fake.word(),
                    status=self.fake.word()
                )
            ) for _ in range(self.fake.random_int(min=1, max=5))
        ]
        return validation_point_models.ValidationPointModel(
            levels=levels,
            metaData=metaData,
            results=results
        )
