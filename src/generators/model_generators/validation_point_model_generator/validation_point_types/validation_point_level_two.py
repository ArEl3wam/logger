from src.dependencies.models.validation_point import ValidationPointModel
from src.generators.model_generators.validation_point_model_generator.abstract_validation_point import \
    AbstractValidationPoint


class ValidationPointLevelTwo(AbstractValidationPoint):
    def __init__(self, mac: int, direction: str, metadata: dict = None):
        super().__init__(metadata)
        self.mac = mac
        self.direction = direction
        if self.direction.lower() not in ("rx", "tx"):
            raise ValueError("Direction must be either Rx or Tx")

    def model(self):
        return ValidationPointModel(
            levels=[{
                "mac": self.mac,
                "direction": self.direction}],
            meta_data=self.metadata
        )


test = ValidationPointLevelTwo(mac=1, direction="rx").model()
print(test)
