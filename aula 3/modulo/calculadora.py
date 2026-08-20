import matematica, matematica_2

# res = matematica.subtracao(10,20, 3, 1)
# res2 = matematica_2.multiplicacao(10, 5, 2)
# res3 = matematica_2.divisao(10, 5, 2)
# print(res2)

oper = input("Digite o operador (+, -, *, /):")
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
res = 0
if oper == "+":
    res = matematica.soma(num1, num2)
elif oper == "-":
    res = matematica.sub(num1, num2)
elif oper == "*":
    res = matematica_2.mult(num1, num2)
elif oper == "/":
    res = matematica_2.div(num1, num2)
else:
    print("invalido")
print(f'O resultade de {num1} {oper} {num2} = {res}')
