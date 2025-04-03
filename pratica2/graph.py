from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

import os

# Gerando alguns dados de exemplo

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CORES = ["b", "g", "r", "c", "m", "y", "k", "w"]

class Equipotencia:
    x: list
    y: list
    tensoes:list
    
    def __init__(self):
        self.x = []
        self.y = []
        self.tensoes = []
    
    def append(self, linha):
            dados = linha.split(';')
            
            self.x.append(float(dados[0]))
            self.y.append(ALFABETO.index(dados[1].upper()) + 1)
            
            self.tensoes.append(float(dados[2]))
    
    def tensaoMedia(self):
        return sum(self.tensoes) / len(self.tensoes)


file1 = r".\\dados\\barras_paralelas.csv"
file2 = r".\\dados\\barras_paralelas_condutor.csv"

with open(os.path.dirname(__file__) + file1) as file:
    dados = file.read()
    grupos = []
    grupo = Equipotencia()
    
    for i, linha in enumerate(dados.splitlines()):
        if(linha):
            grupo.append(linha)
        else:
            grupos.append(grupo)
            grupo = Equipotencia()
            

# Plotando os pontos em diferentes cores para representar diferentes grupos
for i, grupo in enumerate(grupos):    
    plt.scatter(grupo.x, grupo.y, color=CORES[i], alpha=0.6)
    
plt.grid(True, linestyle="--", alpha=0.6, color="gray")
plt.title('Duas chapas')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionando a legenda
plt.legend()

# Exibindo o gráfico
#plt.show()

path = os.path.dirname(__file__) + r"\\image"
print(path)
plt.savefig(path + r"\\" + f"fig_{len(os.listdir(path))}.png")
