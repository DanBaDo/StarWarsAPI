from models.ORMobjects import Character
from models.session import db
from flask import request, jsonify

def addCharacter():
    try:
        new_caracter = Character(**request.json)
        print(new_caracter)
        db.session.add(new_caracter)
        print(new_caracter)
        db.session.commit()
        print(new_caracter)
        return jsonify({"message": "New character added."}), 201
    except Exception as err:
        print(err)
        return jsonify({
            "message": "Error adding character",
            "error": err,
        }), 500
        
def getAllCharacters():
    characters = Character.query.all()
    return jsonify([character.serialize() for character in characters]), 200