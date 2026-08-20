# l = []
# for i in range(10):
#     if i % 2 == 0:
#         l.append(i)
# print(l)

# l2 = [expressao for item in interavel]
#1
l2 = [i**2 for i in range(11)]
print(l2)

#2
l3 = [i for i in range(21) if i % 2 == 0]
print(l3)

#3
palavras = ['python', 'list', 'comprehensions', 'exercicios']
l4 = [len(i) for i in palavras]
print(l4)

#4
calcius = [0, 10, 20, 30, 40]
l5 = [c * 9/5 + 32 for c in calcius]
print(l5)

#5
frutas = ['maçã', 'banana', 'uva', 'morango', 'abacaxi']
l6 = [i for i in frutas if len(i) > 5]
print(l6)

#6
l7 = ['Fizz'  if i % 3 == 0 else i for i in range(21)]
print(l7)