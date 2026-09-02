lis = [1,10,5,6,11,2]
def maior(lista):
    maior = lista[0]
    menor = lista[0]
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