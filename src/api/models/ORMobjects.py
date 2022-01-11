from api.models import db

class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(250), nullable=False)
    password_hash=db.Column(db.String(250))
    def __repr__(self):
        return '<User id: %r - %s>' % (self.id, self.username)
    def serialize(self):
        return { "id": self.id, "username": self.username }

class Character(db.Model):
    __tablename__="character"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(250), nullable=False)
    description=db.Column(db.String(512), nullable=False)
    img_path=db.Column(db.String(256))
    def __repr__(self):
        return '<Character id: %r - %s>' % (self.id, self.name)
    def serialize(self):
        return { "id": self.id, "name": self.name, "description": self.description }

class Planet(db.Model):
    __tablename__="planet"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(250), nullable=False)
    description=db.Column(db.String(512), nullable=False)
    img_path=db.Column(db.String(256))
    def __repr__(self):
        return '<Planet id: %r - %s>' % (self.id, self.name)
    def serialize(self):
        return { "id": self.id, "name": self.name, "description": self.description, "img_path": self.img_path }

class Favorite(db.Model):
    __tablename__="favorite"
    id=db.Column(db.Integer,primary_key=True)
    user_id =db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id =db.Column(db.Integer, db.ForeignKey("planet.id"))
    character_id =db.Column(db.Integer, db.ForeignKey("character.id"))
    user =db.relationship(User)
    planet =db.relationship(Planet)
    character =db.relationship(Character)
