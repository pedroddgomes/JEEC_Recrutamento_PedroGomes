from typing import Dict, Optional
from jeec_app.models.character import Character

class UpdateCharacterService:
    def __init__(self, character: Character, kwargs: Dict):
        self.character = character
        self.kwargs = kwargs

    def call(self) -> Optional[Character]:
        update_result = self.character.update(**self.kwargs)
        return update_result