from flask import request
from flask_jwt_extended import create_access_token
from api.models import User
from werkzeug.security import check_password_hash

def login():
    login_data = request.json
    try:
        user = User.query.filter_by(username = login_data['username'])
        check_password_hash(user.password_hash, login_data["passord"])
    except Exception as err:
        pass
    pass #TODO