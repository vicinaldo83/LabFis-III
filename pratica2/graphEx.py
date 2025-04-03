from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

import os

# Gerando alguns dados de exemplo

CORES = ["b", "g", "r", "c", "m", "y", "k", "w"]

file = r".\\dados\\barras_paralelas_condutor_media.csv"


x = []
y = []

with open(os.path.dirname(__file__) + file) as file:
    dados = file.read()
    for linha in dados.splitlines():
        dado = linha.split(";")
        x.append(float(dado[0]))
        y.append(float(dado[1]))
        
            
# Plotando os pontos em diferentes cores para representar diferentes grupos
plt.plot(x, y, color="g", alpha=0.6)
plt.scatter(x, y, color="g", alpha=0.6)

    
plt.grid(True, linestyle="--", alpha=0.6, color="gray")
plt.title('')
plt.xlabel('Posição')
plt.ylabel('Potencia')

# Adicionando a legenda
plt.legend()

# Exibindo o gráfico
#plt.show()

path = os.path.dirname(__file__) + r"\\image"
print(path)
plt.savefig(path + r"\\" + f"fig_{len(os.listdir(path))}.png")
