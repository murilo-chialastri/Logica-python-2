#empactomento e desempacotamento

def soma(*args):
    res = 0
    for i in args:
        res += i
    return res

def media(*args):
    return soma(*args)/len(args)

def printa(*t):
    txt = ''
    for i in t:
        txt += i
        txt += ' '
    return txt[:-1]

def vezes(*args):
    res = 1
    for i in args:
        res *= i
    return res

print(vezes(1,2,3,4,5,6,7,8,9,10))