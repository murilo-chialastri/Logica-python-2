# l = int(input("Digite a quantidade de linhas: "))
# c = int(input("Digite a quantidade de colunas: "))





matr= [[2,3,1],[2,3,1]]

def soma(matriz):
    soma = 0

    for i in matriz:

        for linha in i:
            soma += linha
    return soma

print(soma(matr))

lis = [1,10,5,6,11,2]
def maior(lista):
    maior = 0
    menor = 0
    numero = 0
    ind = 0
    indm =0

    for i in lista:
        numero = i
        for l in range(len(lista)):
            for j in lista:
                if j > numero:
                    maior = j
            for x in lista:
                if x < numero:
                    menor = x
    for index in range(len(lista)):
        if lista[index] == maior:
            ind = index
    for index in range(len(lista)):
        if lista[index] == menor:
            indm = index
    return maior, menor , ind, indm
print(maior(lis))


def cria_matriz(l, c):
    m = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(int(input("Digite um valor: ")))
        m.append(linha)
    return m

def transposta(matriz):
    m=[]
    for l in range(len(matriz[0])):
        linha = []
        for i in range(len(matriz)):
            linha.append(matriz[i][l])

        m.append(linha)
    return m


matriz = [[1,9,3],[2,4,5],[0,0,0]]
print(matriz)
print(transposta(matriz))
m = transposta(matriz)


for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j],end=" ")
    print("")

for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j],end=" ")
    print("")

for i in range(len(m)):
    for j in range(len(m[0])):
        print(f'm[{i}][{j}] = {m[i][j]}')
