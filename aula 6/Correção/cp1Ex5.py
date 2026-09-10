# A)
desc = lambda x: 0.9*x

# B)
precos = [10.0, 23.5, 3.0, 102.0]
precos2 = [desc(i) for i in precos]

# C)
precos3 = [desc(i) for i in precos if desc(i) > 20]
precos4 = [i for i in precos2 if i > 20]
