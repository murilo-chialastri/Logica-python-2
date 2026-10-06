# l = [12,68,95,41,10,71]
l = [10, 9, 8, 7,22, 3, 1]

print(l)



for i in range(1, len(l)):
    chave = l[i]
    j = i - 1
    while j >= 0 and l[j] > chave:
        l[j + 1] = l[j]
        j = j - 1
        print(f'dentro do while: {l}')
    l[j + 1] = chave
    print(f'no for: {l}')
print(f'organizada: {l}')
# def funcao(l, i):
#     aux = l[i]
#
#     while True:
#         j = len(l)-1
#         if j == 0:
#             break
#         if aux < l[j]:
#
#             l[j-1] = l[j]
#             l[j] = aux
#         j = j -1
#
#         print(l)
#
# funcao(l,3)

# j = 0
# while j < len(l):
#
#     print(j)
#     if j + 1 < len(l):
#         if l[j] > l[j + 1]:
#             aux = l[j]
#             l[j + 1] = l[j]
#     print(l)
#     j+=1
# for j in range( len(l)):
#     print(j)
#     if j+1 < len(l):
#         if l[j] > l[j+1]:
#             aux = l[j]
#             l[j+1] = l[j]
#     print(l)


