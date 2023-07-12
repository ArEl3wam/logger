class AbstractValidationPoint:
    def __init__(self, metadata=None):
        if metadata is None:
            metadata = dict({"Additional Information": "No additional information provided"})
        self.metadata = metadata

    def model(self):
        raise NotImplementedError
