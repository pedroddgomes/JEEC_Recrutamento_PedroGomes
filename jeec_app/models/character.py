from sqlalchemy import Column, String, Integer, Boolean, DateTime, func
from database import Base
from jeec_app.models.model_mixin import ModelMixin

class Character(Base, ModelMixin):
    __tablename__ = "characters"

    # Table info
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Character info
    name = Column(String, nullable=False)
    age = Column(Integer)
    birthday = Column(String)
    gender = Column(String)
    alive = Column(Boolean)


    def __repr__(self):
        return f"<Example {self.id}>"
