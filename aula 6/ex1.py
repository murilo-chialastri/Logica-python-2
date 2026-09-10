d = {
    'lat': 1.85,
    'long': 20.45
}
d['lat'] = 100
d['nova'] = 'teste'
print(d['nova'])


print(d.get('long'))
d.pop('nova')
# a = 'lat' in d
# print(a)
# for i in d.keys():
#     print(i)
# for j in d.values():
#     print(j)
#
# for k in d.items():
#     print(k)


for k, l in d.items():
    print(f'chave: {k} | valor: {l}')