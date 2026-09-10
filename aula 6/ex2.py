frutas = {
    'uva': 'roxo',
    'morango': 'vermelho',
    'banana': 'amarelo',
}
print(frutas['uva'])

frutas['laranja'] = 'laranja'

frutas['uva'] = 'verde'

frutas.pop('laranja')

for i in frutas.keys():
    print(i)

for i in frutas.values():
    print(i)
existe = 'banana' in frutas

frutas2 = {
    'pera': 'amarelo',
    'melancia': 'verde',
}
frutas.update(frutas2)


print('dicionario')
print(frutas)

contador = 0
for i in frutas.items():
    for j in i:
        contador += 1

print(contador)





