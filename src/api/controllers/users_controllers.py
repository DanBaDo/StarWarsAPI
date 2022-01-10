from flask import request, jsonify

from api.models.ORMobjects import User
from api.models.session import db
from tools.password_hash import get_password_hash

def add_user():
    user_data = request.json
    try:
        if "username" in user_data and "password" in user_data :
            password_hash = get_password_hash(user_data["password"])
            new_user = User(username=user_data["username"], password_hash=password_hash)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "New user added."}), 201
        else:
            return jsonify({
                "message": "Must provide user and password",
            }), 400
    except Exception as err:
        print(err)
        return jsonify({
            "message": "Error adding user",
            "error": err,
        }), 500
def get_all_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user: return jsonify(user.serialize()), 200
    return jsonify({"message": "User id: %s not found" % user_id}), 404