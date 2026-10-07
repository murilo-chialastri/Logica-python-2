import requests


def buscaPokemon():
    pokemon = input("Digite o nome do pokemon: ")
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    api = requests.get(url)
    json = api.json()
    id = json['id']

    return id

# teste = buscaPokemon()
# print(teste)

def organizaPokemon(l):
    for i in range(1,len(l)):
        chave = l[i]
        j = i -1
        while j >= 0 and l[j] > chave:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = chave
    return l



pokemon = []
for i in range(5):
    pk = buscaPokemon()
    pokemon.append(pk)
    print(pokemon)
print(organizaPokemon(pokemon))
# print(f'antes: {pokemon}')
# org = organizaPokemon(pokemon)
# print(f'Depois: {org}')
# print(lista)
# print(organizaPokemon(lista))
# print(l)
# for i in range(1, len(l)):
#     chave = l[i]
#     j = i - 1
#     while j >= 0 and l[j] > chave:
#         l[j + 1] = l[j]
#         j = j - 1
#     l[j + 1] = chave
# print(l)
