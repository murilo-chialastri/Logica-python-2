# l2 = [[1,2,3],
#       [4,5,6],
#       [7,8,9]]
#
# print(l2)
# for i in l2:
#     print(i)
# print(m)

l1 = [10,2]
l2 = [21,13]
l3 = [7,9]

#     #0  1
# m = [
#     [10,2], # 0
#     [21,13], # 1
#     [7,9]]  # 2
# print(m[1][1])

m = [l1]
m.append(l2)
m.insert(2,l3)
print(m)

linha = int(input('Digite a qtde de linhas:'))
coluna = int(input('Digite a qtde de colunas:'))

m = []
for j in range(linha):
    l = []
    for i in range(coluna):
        l.append(int(input(f'Digite o elemento a[{j}][{i}]:')))
    m.append(l)
print(m)

for i in m:
    print(*i)