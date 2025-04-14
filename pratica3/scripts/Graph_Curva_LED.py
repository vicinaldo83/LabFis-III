from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

import os

# Gerando alguns dados de exemplo

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CORES = ["black", "blue", "red"]

files = [
    os.path.dirname(__file__) + r"\..\dados\4\curvaVxI_diodo.csv",
    os.path.dirname(__file__) + r"\..\dados\4\curvaVxI_led_azul.csv",
    os.path.dirname(__file__) +  r"\..\dados\4\curvaVxI_led_vermelho.csv"
]

img_dir = os.path.dirname(__file__) + r"\\..\\images\\VxI_LED\\"
os.makedirs(img_dir, exist_ok=True)

def parse_data(data:str):
    I = []
    V = []
    
    for line in data.strip().splitlines()[1:]:
        V.append(float(line.split(";")[0]))
        I.append(float(line.split(";")[1]))
        
    return V, I


for i, (file, color) in enumerate(zip(files[1:], CORES[1:])):
    with open(file) as data:
        V, I = parse_data(data.read())
        plt.plot(V, I, color=color, alpha=0.6)
    
        
plt.grid(True, linestyle="--", alpha=0.6, color="gray")
plt.title('Duas chapas')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.savefig(img_dir + r"\\" + f"{len(os.listdir(img_dir))}.png")
