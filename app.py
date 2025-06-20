from flask_migrate import Migrate
from flask import Flask, jsonify, request
from database import engine, Base, db_session
from jeec_app.handlers.character_handler import CharacterHandler
from jeec_app.finders.character_finder import CharacterFinder
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

    # route to fetch a character info
    @app.route("/characters/search", methods=["GET"])
    def search_characters():
        # Get query parameters
        name = request.args.get("name")
        age = request.args.get("age")
        birthday = request.args.get("birthday")
        gender = request.args.get("gender")
        alive = request.args.get("alive")

        results = []

        if name:
            results = CharacterFinder.get_by_name(name)
        elif age:
            results = CharacterFinder.get_by_age(int(age))
        elif birthday:
            results = CharacterFinder.get_by_birthday(birthday)
        elif gender:
            results = CharacterFinder.get_by_gender(gender)
        elif alive is not None:
            results = CharacterFinder.get_by_alive(alive.lower() == "true")
        else:
            return jsonify({"error": "No search parameter provided"}), 400

        return jsonify([
            {
                "id": c.id,
                "name": c.name,
                "age": c.age,
                "birthday": c.birthday,
                "gender": c.gender,
                "alive": c.alive
            }
            for c in results
        ])
    

    # route to create one
    @app.route("/characters", methods=["POST"])
    def create_character():
        data = request.json
        print(">>> Incoming character data:", data)
        result = CharacterHandler.create_character(**data)
        print(">>> Created character:", result)
        if result is None:
            return jsonify({"error": "Could not create character"}), 500
        return jsonify({"status": "success", "id": result.id}), 201
    

    # route to delete character
    @app.route("/characters/<int:id>", methods=["DELETE"])
    def remove_character(id):
        character = CharacterFinder.get_from_id(id=id)
        if not character:
            return jsonify({"error": f"Character {id} not found"}), 404

        success = CharacterHandler.delete_character(character=character)
        if success:
            return jsonify({"message": f"Removed character {id}"}), 200
        else:
            return jsonify({"error": "Failed to delete character"}), 500


    # route to update character 
    @app.route("/characters/<int:id>", methods=["PUT"])
    def update_character(id):
        character = CharacterFinder.get_from_id(id=id)
        if not character:
            return jsonify({"error": f"Character {id} not found"}), 404

        data = request.json
        result = CharacterHandler.update_character(character=character, **data)

        if result is None:
            return jsonify({"error": "Failed to update character"}), 500

        return jsonify({
            "message": f"Character {id} updated",
            "updated": {
                "id": result.id,
                "name": result.name,
                "age": result.age,
                "birthday": result.birthday,
                "gender": result.gender,
                "alive": result.alive
            }
        }), 200
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)