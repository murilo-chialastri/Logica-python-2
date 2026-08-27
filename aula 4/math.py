import matplotlib.pyplot as plt

# Coordenadas x e y
x = [i for i in range(-100, 101)]
y = [i ** 3 for i in x]

# Plotando o gráfico
# marker='o' para usar círculos, linestyle='-' para usar uma linha sólida
plt.plot(x, y, marker='o', linestyle='-')

plt.title('Gráfico de Coordenadas x, y')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)  # Adiciona uma grade ao gráfico
plt.show()

# amo o professor

