# numero1 = float(input('digite o primeiro numero: '))
# numero2 = float(input('digite o segundo numero: '))
# res = (numero1 * 2) * (numero2 * 3)
# print(res)
passou = []
notas = []
qut = int(input("Quantos notas? "))
a = 0
while a < qut:
    nt = float(input("escreva a nota "))
    a += 1
    notas.append(nt)

i = 0
while i < len(notas):
    print(notas[i])
    if (notas[i] >= 6):
        passou.append(notas[i])
    i += 1

print(passou)
print(notas)

