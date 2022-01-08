from controllers.characters_controllers import add_character, get_all_characters, get_character_by_id

def add_character_endpoints (app):
    app.add_url_rule("/characters/", methods=["GET"], view_func=get_all_characters)
    app.add_url_rule("/characters/<int:character_id>/", methods=["GET"], view_func=get_character_by_id)
    app.add_url_rule("/characters/", methods=["POST"], view_func=add_character)
