from jeec_app.services.character.create_character_service import CreateCharacterService
from jeec_app.services.character.delete_character_service import DeleteCharacterService
from jeec_app.services.character.update_character_service import UpdateCharacterService

class CharacterHandler:
    @classmethod
    def create_character(cls, **kwargs):
        return CreateCharacterService(kwargs={**kwargs}).call()
    
    @classmethod
    def update_character(cls, character ,**kwargs):
        return UpdateCharacterService(character=character, kwargs={**kwargs}).call()
    
    @classmethod
    def delete_character(cls, character):
        return DeleteCharacterService(character=character).call()