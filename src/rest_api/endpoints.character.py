from main import app
from controllers.characters_controllers import addCharacter, getAllCharacters
app.add_url_rule("/characters/", methods=["POST"], view_func=addCharacter)
