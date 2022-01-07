# Standar modules imports
from os import environ
# Pip modules imports
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
# Local imports
from models.session import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_CONNECTION_STRING')

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

if __name__ == '__main__':
    PORT = int(environ.get('FLASK_PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)