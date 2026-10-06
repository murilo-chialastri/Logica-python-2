def lista_binaria (lista, busca):
    menor = 0
    maior = len(lista) -1
    # print(l,r)
    while menor<=maior:

        meio = (menor + maior)//2
        if lista[meio] > busca:
            maior = meio - 1
        elif lista[meio] < busca:
            menor = meio + 1
        else:
            return meio
    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = lista_binaria(lista, 4)
print(a)