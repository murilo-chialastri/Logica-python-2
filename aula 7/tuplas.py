# a = (1, 10, True, 'Ok')
# b= [2,3,4,5,6]
# c = tuple(b)
# d = list(c)
# print(type(d))

# for i, j in enumerate(c):
#     print(i, j)

# 1
tupla = (2,'ads',True)
add = 'adicionado'
re = 0
def addTupla(tup, add):
    # tup = list(tup)
    # tup.append(add)
    # tup  = tuple(tup )
    # return tup
    return tup + (add,)

tupla = addTupla(tupla, add)
print(tupla)


def remover (tup, index):
    tup = list(tup)
    tup.pop(index)
    tup = tuple(tup)
    return tup

tupla = remover(tupla, 2)
print(tupla)