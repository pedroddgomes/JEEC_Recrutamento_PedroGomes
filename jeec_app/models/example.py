from sqlalchemy import Column, String, Integer, DateTime, func
from database import Base
from jeec_app.models.model_mixin import ModelMixin

class Example(Base, ModelMixin):
    __tablename__ = "example"

    id = Column(Integer, primary_key=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    body = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Example {self.id}>"
