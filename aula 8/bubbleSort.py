lista = [12,68,95,41,25,71]


print(lista)

for j in range(len(lista)-1,0,-1):
    for i in range(j):
        if lista[i] > lista[i+1]:
            ax = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = ax
    print(lista)

