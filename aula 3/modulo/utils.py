def contar_vogal(texto):
    letra = ['a','e','i','o','u']
    vogal = 0
    for i in texto:
        if i in letra:
            vogal += 1
    return vogal

def reverter(texto):
    texto = texto[::-1]
    return texto

def contar_palavras(texto):
    espaco = ' '
    quantidade = 1
    for i in texto:
        if i in espaco:
            quantidade += 1
    return quantidade



