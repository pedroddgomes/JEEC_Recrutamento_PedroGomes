import logging
from jeec_app.models.example import Example
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class CreateExampleService:
    def __init__(self, kwargs: Dict):
        self.kwargs = kwargs

    def call(self) -> Optional[Example]:

        example = Example.create(**self.kwargs)

        if not example:
            return None

        return example