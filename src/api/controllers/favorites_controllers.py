from api.models.ORMobjects import Character, Planet, User
from flask import jsonify

def add_favorite_planet(user_id, planet_id):
    try:
        User.query.get(user_id).planets.append(
            Planet.query.get(planet_id)
        )
    except Exception as err:
        print(err)
        return jsonify({
            "message": "Error adding new favorite planet",
            "error": err,
        }), 500

def get_favorite_planets(user_id):
    return jsonify(
        (planet.serialize() for planet in User.get(user_id).planets)
    )

def drop_favorite_planet(user_id, planet_id):
    try:
        User.query.get(user_id).planets.remove(
            Planet.query.get(planet_id)
        )
    except Exception as err:
        print(err)
        return jsonify({
            "message": "Error removing favorite planet",
            "error": err,
        }), 500

def add_favorite_character(user_id, character_id):
    try:
        User.query.get(user_id).characters.append(
            Character.query.get(character_id)
        )
    except Exception as err:
        print(err)
        return jsonify({
            "message": "Error adding new favorite character",
            "error": err,
        }), 500

def get_favorite_characters(user_id):
    return jsonify(
        (character.serialize() for character in User.get(user_id).characters)
    )

def drop_favorite_character(user_id, character_id):
    try:
        User.query.get(user_id).characters.remove(
            Character.query.get(character_id)
        )
    except Exception as err:
        print(err)
        return jsonify({
            "message": "Error removing favorite character",
            "error": err,
        }), 500