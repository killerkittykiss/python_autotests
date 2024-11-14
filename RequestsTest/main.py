import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'токен'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Alexi",
    "photo_id": 19
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

id_pokemon = response_create.json()['id']
print(id_pokemon)

body_change = {
    "pokemon_id": id_pokemon,
    "name": "Murrr",
    "photo_id": 366
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

body_pokeball = {
    "pokemon_id": id_pokemon
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)

