saldo = 0
trans = []

def depositar(valor):
    global saldo
    saldo = saldo + valor
    trans.append(valor)

def sacar(valor):
    global saldo
    saldo = saldo - valor
    trans.append(-valor)

def extrato():
    for i in trans:
        print(f'R${i:.2f}')
    print('-----------')
    print(f'R${saldo:.2f}')

while True:
    op = input('Digite (1) para saque; (2) para deposito; (3) para extrato; (4) para sair:')
    if op == '1':
        valor = float(input('Digite o valor do saque: '))
        sacar(valor)
    elif op == '2':
        valor = float(input('Digite o valor do deposito: '))
        depositar(valor)
    elif op == '3':
        extrato()
    elif op == '4':
        break
    else:
        print('Opção inválida!')