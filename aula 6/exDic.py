dados = [
    {'dia':12,'mes':2,'ano':2019,'temp':30.5},
    {'dia':18,'mes':3,'ano':2019,'temp':29.1},
    {'dia':22,'mes':4,'ano':2019,'temp':28.5},
    {'dia':17,'mes':5,'ano':2019,'temp':26.4},
]

for i in range(len(dados)):
    print(f'# {dados[i]['dia']}/{dados[i]['mes']:02d}/{dados[i]['ano']}: Temperatura:{dados[i]['temp']}')



