import requests
pokemon = input("Digite o nome do pokemon: ")
url =f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
api = requests.get(url)
json = api.json()
pokedex = json['id']
tipo = json['types']
tipo1 = tipo[0]['type']['name']
tipo2 = tipo[1]['type']['name']
tipos = [tipo1, tipo2]


print(f'Pokemon {pokemon}| Pokedex {pokedex} tipo {tipos}')