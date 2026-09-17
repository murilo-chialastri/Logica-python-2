def contLetra (frase):
    cont = {}
    contador = 0
    for i in frase:
        # if i in cont:
        #   cont[i] = d[i] + 1
        # else:
        #   d[i] = 1
        for j in frase:
            if i == j:
                contador += 1
        cont[i] = contador
        contador = 0


    return cont
print(contLetra('os ratos'))

def verAnagramas (frase1, frase2):
    cont1 = contLetra(frase1)
    cont2 = contLetra(frase2)
    # print(f'{cont1} \n{cont2}')
    if cont1 == cont2:
        return True
    else:
        return False
print(verAnagramas('ratos', 'sotar'))

