linha = int(input('Digite a qtde de linhas:'))
coluna = int(input('Digite a qtde de colunas:'))

m = []
for j in range(linha):
    l = []
    for i in range(coluna):
        l.append(i + j*coluna + 1 )
    m.append(l)
print(m)