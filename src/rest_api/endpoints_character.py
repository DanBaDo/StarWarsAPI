from controllers.characters_controllers import addCharacter, getAllCharacters

def add_character_endpoints (app):
    app.add_url_rule("/characters/", methods=["POST"], view_func=addCharacter)
    app.add_url_rule("/characters/", methods=["GET"], view_func=getAllCharacters)
