import logging
from jeec_app.models.character import Character
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class CreateCharacterService:
    def __init__(self, kwargs: Dict):
        self.kwargs = kwargs

    def call(self) -> Optional[Character]:

        character = Character.create(**self.kwargs)

        if not character:
            logger.error("Character creation failed.")
            return None

        return character