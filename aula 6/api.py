import requests

cep = input('Digite o CEP: ')
url = f'https://viacep.com.br/ws/{cep}/json/'

a = requests.get(url)
b = a.json()
print(b)

print(f'Bairro: {b["bairro"]}'
      f'\nCidade: {b["localidade"]}'
      f'\nRua: {b["logradouro"]}')
