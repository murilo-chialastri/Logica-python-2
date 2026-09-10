from multiprocessing import context


def matriz(l,c):
    m = []
    # cont = 1
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(j*c+i+1)
            # cont+= 1
        m.append(linha)
    return m

print(matriz(3,3))