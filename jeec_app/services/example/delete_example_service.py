from jeec_app.models.example import Example

class DeleteExampleService:
    def __init__(self, example: Example):
        self.example = example

    def call(self) -> bool:
        result = self.example.delete()
        return result