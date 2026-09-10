
def f(x):
    if x <= -2:
        return x**2 + 3*x - 4
    elif x < 0:
        return 2*x + 5
    elif x < 4:
        return x**(1/2)
    elif x < 6:
        return x**3 - 3* x**2 - 10 *x
    elif x < 8:
        return x**2 - 4*x - 20
    else:
        return 20

import matplotlib.pyplot as plt

# Coordenadas x e y
x = [i*20/2000 for i in range(-1000, 1000)]
y = [f(i) for i in x]

# Plotando o gráfico
# marker='o' para usar círculos, linestyle='-' para usar uma linha sólida
plt.plot(x, y, marker='o', linestyle='-')

plt.title('Gráfico de Coordenadas x, y')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)  # Adiciona uma grade ao gráfico
plt.show()

# amo o professor



