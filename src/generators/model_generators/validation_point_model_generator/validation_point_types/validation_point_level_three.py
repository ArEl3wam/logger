from src.dependencies.models.validation_point import ValidationPointModel
from src.generators.model_generators.validation_point_model_generator.abstract_validation_point import AbstractValidationPoint


class ValidationPointLevelThree(AbstractValidationPoint):
    def __init__(self, mac: int, direction: str, packet_id: int, metadata: dict = None):
        super().__init__(metadata)
        self.mac = mac
        self.direction = direction
        self.packet_id = packet_id
        if self.direction.lower() not in ("rx", "tx"):
            raise ValueError("Direction must be either 'Rx' or 'Tx' as string")

    def model(self):
        return ValidationPointModel(
            levels=[{
                "mac": self.mac,
                "direction": self.direction,
                "packet Identifier": self.packet_id}
            ],
            meta_data=self.metadata
        )
