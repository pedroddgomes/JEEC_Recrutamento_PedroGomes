from flask_migrate import Migrate
from flask import Flask, jsonify, request
from database import engine, Base, db_session
from jeec_app.handlers.character_handler import CharacterHandler
from jeec_app.finders.example_finder import ExampleFinder
import os
from dotenv import load_dotenv

from jeec_app.models.character import Character

# TO CREATE NEW TABLES U NEED TO IMPORT THE MODELS HERE AND RUN THE initDB.py

def create_app():
    app = Flask(__name__)
    load_dotenv()  # Load environment variables

    # current_path = os.path.dirname(os.path.realpath(__file__))
    # migrations_dir = os.path.join(current_path, "jeec_app", "database", "migrations")
    # migrate = Migrate(app, db_session, directory=migrations_dir)

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Clean up database session after each request
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @app.route("/", methods=["GET"])
    def hello():
        return "Hello from Flask"

    # Example route to fetch by ID
    @app.route("/get_example/<int:id>", methods=["GET"])
    def get_example(id):
        example = ExampleFinder.get_from_id(id=id)
        if example:
            return jsonify({"id": example.id, "body": example.body})
        return jsonify({"error": "Example not found"}), 404

    # Example route to create one
    @app.route("/characters", methods=["POST"])
    def create_character():
        data = request.json
        print(">>> Incoming character data:", data)
        result = CharacterHandler.create_character(**data)
        print(">>> Created character:", result)
        if result is None:
            return jsonify({"error": "Could not create character"}), 500
        return jsonify({"status": "success", "id": result.id}), 201
    
    @app.route("/remove_example/<int:id>", methods=["POST"])
    def remove_example(id):
        example = ExampleFinder.get_from_id(id=id)
        if example:
            result = CharacterHandler.delete_example(example=example)
            print(result)

        return jsonify({"message": f"Removed example {id}"}), 200
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)