from typing import Dict, Optional
from jeec_app.models.example import Example

class UpdateExampleService:
    def __init__(self, example: Example, kwargs: Dict):
        self.example = example
        self.kwargs = kwargs

    def call(self) -> Optional[Example]:
        update_result = self.example.update(**self.kwargs)
        return update_result