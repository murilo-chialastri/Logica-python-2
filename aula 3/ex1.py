carrinho = []
def carrinhoAdd (produtos):
    carrinho.append(produtos)

def carrinhoRemover(produtos):
    # carrinho.remove(produtos) (funciona)
    for i in range (len(carrinho)):
        if carrinho[i][1] == produtos:
            carrinho.pop(i)
            break

def verCarrinho():
    for produtos in carrinho:
        print(produtos)

while True:
    op = input("1 add / 2 remove / 3 carrinho ")
    if op == '1':
        produto = input("Digite o nome do produto: ")
        carrinhoAdd(produto)
    elif op == '2':
        produto = input("Digite o nome do produto para remover: ")
        carrinhoRemover(produto)
    elif op == '3':
        verCarrinho()
    else:
        print("opcão invalida")