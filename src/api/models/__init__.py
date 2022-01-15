from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from api.models.ORMobjects import User, Character, Planet, Favorite