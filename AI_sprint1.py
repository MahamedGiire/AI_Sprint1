import json


def load_json(file_name):
    """Deze functie zorgt ervoor dat het json bestand wordt geladen in Python."""
    steam_json_file = open(file_name, 'r')
    steam_json_data = steam_json_file.read()
    steam_json_load = json.loads(steam_json_data)
    return steam_json_load


steam_json = load_json('steam_JSON_file.json')


def first_name():
    """Deze functie zorgt ervoor dat de eerste naam uit het json bestand wordt teruggegeven."""
    return steam_json[0]["name"]


def return_game(name):
    """Deze functie geeft de gegevens van de ingevoerde game terug.
    Als deze niet bestaat, wordt hiervan een bericht geprint."""
    for game in range(len(steam_json)):
        if steam_json[game]["name"] == name:
            return steam_json[game]
        else:
            continue

    return 'Game not found'


def create_dict():
    """Deze functie zorgt ervoor dat er een dictionary wordt gemaakt met daarin als key alle namen van de games
    en als values nog een dictonary met alle waardes van deze games."""
    steam_json_dict = {}

    for i in range(len(steam_json)):
        game_dict = {}
        for index in steam_json[i]:
            game_dict[index] = steam_json[i][index]
        steam_json_dict[steam_json[i]["name"]] = game_dict

    return steam_json_dict


def sort_dict(dict):
    """Deze functie sorteert een meegegeven dictionary"""
    return sorted(dict.keys())


#print(create_dict())
#print(sort_dict(create_dict()))
print(return_game("Portal"))

