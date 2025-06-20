from jeec_app.services.example.create_example_service import CreateExampleService
from jeec_app.services.example.delete_example_service import DeleteExampleService
from jeec_app.services.example.update_example_service import UpdateExampleService

class ExampleHandler:
    @classmethod
    def create_example(cls, **kwargs):
        return CreateExampleService(kwargs={**kwargs}).call()
    
    @classmethod
    def update_example(cls, example ,**kwargs):
        return UpdateExampleService(example=example, kwargs={**kwargs}).call()
    
    @classmethod
    def delete_example(cls, example):
        return DeleteExampleService(example=example).call()