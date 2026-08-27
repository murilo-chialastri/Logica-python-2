import random


while True:
    lin = int(input("Informe as linhas: "))
    col = int(input("Informe as colunas: "))
    if lin > 0 and col > 0:
        m = []
        for i in range(lin):
            linha = []
            for j in range(col):
                num = random.randint(0,9)
                linha.append(num)
            m.append(linha)
        break
    else:
        print("precisa ser maior que 0")


for i in range(lin):
    for j in range(col):
        print(m[i][j],end=" ")
    print("")
