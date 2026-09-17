lista1 = [1, 5, 3, 7, 8]
lista2 = [1, 2, 3, 4, 5]

c1 = set(lista1)
c2 = set(lista2)

comum = c1 & c2
print(comum)

exisPrimeira = c1 - c2
print(exisPrimeira)
existSegunda = c2 - c1
print(existSegunda)

naoRep = c1 ^ c2
# noaRep = (c1 - c2) | (c2 - c1)
# naoRep = (c1 | c2) - (c1 & c2)
print(naoRep)
print(naoRep)
