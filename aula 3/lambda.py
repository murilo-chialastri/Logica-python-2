import string

soma = lambda a, b, c: a + b + c
res = soma(4, 5, 3)
print(res)

inverter = lambda p: p[::-1]
print(inverter('string'))

palindromo = lambda p: p == p[::-1]
print(palindromo('ola'))