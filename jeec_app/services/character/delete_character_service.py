from jeec_app.models.character import Character

class DeleteCharacterService:
    def __init__(self, character: Character):
        self.character = character

    def call(self) -> bool:
        result = self.character.delete()
        return result