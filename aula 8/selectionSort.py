lista = [12,68,95,41,10,71]




def selectionSort(lista):
    n = len(lista)
    for i in range(n-1):
        min_index = i
        for j in range(i,n):
            if lista[j] < lista[min_index]:
                min_index = j
        if lista[i] > lista[min_index]:
            aux = lista[i]
            lista[i] = lista[min_index]
            lista[min_index] = aux

print(lista)
selectionSort(lista)
print(lista)
# def menorElemento(l, index):
#     imenor = index
#     menor = l[imenor]
#     for i in range(imenor, len(l) ):
#         if l[i] < menor:
#             menor = l[i]
#             imenor = i
#     return imenor
#
# menor = menorElemento(lista, 5)
#
# for k in range(len(lista)):
#     j = menorElemento(lista, k)
#     aux = lista[j]
#     lista[j] = lista[k]
#     lista[k] = aux
#     print(lista)
#     print()