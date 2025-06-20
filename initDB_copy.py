from database import Base, engine
from app import create_app  # Import the factory function

app = create_app()

with app.app_context():
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully.")
