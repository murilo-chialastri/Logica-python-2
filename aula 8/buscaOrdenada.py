lista = [1,2,4,5,8,9]
id = 4
for i in range(len(lista)):
    print(lista[i])
    if id == lista[i]:
        index = i
        break
print(f'index:{index}')
