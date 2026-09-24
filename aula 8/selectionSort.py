lista = [12,68,95,41,10,71]


def menorElemento(l, index):
    imenor = index
    menor = l[imenor]
    for i in range(imenor, len(l) ):
        if l[i] < menor:
            menor = l[i]
            imenor = i
    return imenor

menor = menorElemento(lista, 5)

for k in range(len(lista)):
    j = menorElemento(lista, k)
    aux = lista[j]
    lista[j] = lista[k]
    lista[k] = aux
    print(lista)
    print()