from src.dependencies.models.validation_point import ValidationPointModel
from src.generators.model_generators.validation_point_model_generator.abstract_validation_point import AbstractValidationPoint


class ValidationPointLevelOne(AbstractValidationPoint):
    def __init__(self, mac: int, metadata: dict = None):
        super().__init__(metadata)
        self.mac = mac

    def model(self):
        return ValidationPointModel(
            levels=[{
                "mac": self.mac}],
            meta_data=self.metadata
        )
