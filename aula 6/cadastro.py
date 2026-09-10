dicionario = {

}
while True:
    nome = input('Digite seu nome: ')
    if nome == '':
        break
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))

    dicionario[nome] = {'idade': idade, 'altura': altura}
    print(dicionario)

print(dicionario)