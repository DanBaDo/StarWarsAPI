from api.models.ORMobjects import Favorite, User
from api.models import db
from flask import request, jsonify
from flask_sqlalchemy import and_

'''
TODO:
add_favorite_planet, add_favorite_character
drop_favorite_planet, drop_favorite_character
get_favorite_planets, get_favorite_characters
'''

def add_favorite_planets(user_id, planet_id):
    '''try:
        new_favorite = Favorite(user_id, planet_id)
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({"message": "New favorite planet added."}), 201
    except Exception as err:
        print(err)
        return jsonify({
            "message": "Error adding new favorite planet",
            "error": err,
        }), 500'''

def get_favorite_planets(user_id):
    '''favorite_plantes = User.get(user_id).favorites.filter_by(Favorite.planet_id != None).with_entities(Favorite.planet_id)'''


def drop_favorite_planets():
    pass

def add_favorite_characters(user_id, character_id):
    try:
        new_favorite = Favorite(user_id, character_id)
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({"message": "New favorite character added."}), 201
    except Exception as err:
        print(err)
        return jsonify({
            "message": "Error adding new favorite character",
            "error": err,
        }), 500

def get_favorite_characters():
    pass

def drop_favorite_character():
    pass