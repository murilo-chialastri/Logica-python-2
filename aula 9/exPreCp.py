    # 1) Escreva uma função que receba uma lista de strings como
    # argumento e retorne um dicionário onde as chaves sejam as
    # palavras e os valores sejam o número de vezes que essas palavras
    # aparecem na lista. Exemplo de entrada:
    # palavras = ["casa", "carro", "casa", "bicicleta", "carro", "carro", "bicicleta"]
    # Exemplo de saída:   {"casa": 2, "carro": 3, "bicicleta": 2}
palavras = ["casa", "carro", "casa", "carro", "carro", "bicicleta"]

def criaDicionario(l):
    dicionario = {}
    for i in l:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] = dicionario[i] + 1
    return dicionario
# print(criaDicionario(palavras))

#  Dada a tupla pessoas = (("João", 19), ("Maria", 21), ("Pedro", 20), ("Ana", 18)),
#  escreva uma função que receba uma tupla semelhantea pessoas e retorne uma nova
#  tupla contendo apenas as pessoas que são maiores de idade (idade ≥ 18).

pessoas = (("João", 19), ("Maria", 1), ("Pedro", 20), ("Ana", 18))

def fiscal(t):
    aux = []
    for i in t:
        print(f'i: {i}')
        if i[1] >= 18:
            aux.append(i)
    aux = tuple(aux)
    return aux
# print(fiscal(pessoas))

# Implemente uma função que receba uma lista de números inteiros
# e ordene essa lista utilizando o algoritmo de Bubble Sort

num = [3,2,5,1,4]
def bolha(lista):

    for x in range(len(lista) - 1, 0, -1):  # contagem regressiva(faz com que a lista seja chamada menos vezes)
        for i in range(x):
            if lista[i] > lista[i + 1]:
                ax = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = ax
    return lista
# print(bolha(num))

def insertion(l):
    for i in range(1, len(l)):
        chave = l[i]
        j = i - 1
        while j >= 0 and l[j] > chave:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = chave
    return l
# print(insertion(num))

# 6) Imagine que você tem um dicionário que armazena o saldo de várias contas bancárias.
# Escreva uma função que receba o dicionário de contas e um segundo dicionário contendo valores
# a serem creditados ou debitados das respectivas contas. A função deve atualizar o saldo das contas
# existentes e criar novas entradas para contas que ainda não existem.
# Exemplo de entrada:
# saldos = {"Conta A": 1000, "Conta B": 1500}
# movimentacoes = {"Conta A": -200, "Conta C": 500}
# Exemplo de saída:
# {"Conta A": 800, "Conta B": 1500, "Conta C": 500}

saldos = {"Conta A": 1000, "Conta B": 1500}
movimentacoes = {"Conta A": -200, "Conta C": 500}

def movimentar(sald, mov):
    total = {}
    for i in sald:
        total[i] = sald[i]
    for i in mov:
        if i in total:
            total[i] = total[i] + mov[i]
        else:
            total[i] = mov[i]

    return total
# print(movimentar(saldos, movimentacoes))

# 7) Escreva uma função que receba uma lista de palavras e ordene-a em ordem alfabética
# utilizando o algoritmo Bubble Sort. Exemplo de entrada:
# palavras = ["banana", "maçã", "laranja", "uva", "abacaxi"]
# Exemplo de saída:
# ["abacaxi", "banana", "laranja", "maçã", "uva"]

frutas = ["banana", "maçã", "laranja", "uva", "abacaxi"]

def ordenar(lista):
    for i in range(len(lista) - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista
# print(ordenar(frutas))

# 8) Escreva uma função que receba um dicionário com o nome de produtos e
# seus respectivos preços, e um valor limite. A função deve retornar um novo dicionário
# contendo apenas os produtos cujo preço seja maior que o limite fornecido.
# Exemplo de entrada:
# produtos = {"banana": 2.50, "maçã": 3.20, "laranja": 1.80}
# limite = 2.00
# Exemplo de saída:
# {"banana": 2.50, "maçã": 3.20}

produtos = {"banana": 2.50, "maçã": 3.20, "laranja": 1.80}
limite = 2.00

def limites(disc,li):
    novo = {}
    for i in disc:
        aux = disc[i]
        print(aux)
        if aux > li:
            novo[i] = disc[i]

    return novo
a = limites(produtos,limite)
print(a)

# 4) Escreva uma função que receba uma lista de tuplas, onde cada tupla contém dois números inteiros.
# A função deve retornar uma lista contendo a soma de cada par de números nas tuplas.
# Exemplo de entrada:
# pares = [(1, 2), (3, 4), (5, 6)]
# Exemplo de saída:
# [3, 7, 11]
pares = [(1, 2), (3, 4), (5, 6)]

def cont_tupla(t):
    lista = []
    for i in t:
        lista.append(i)
