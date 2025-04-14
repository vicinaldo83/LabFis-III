from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

import os

# Gerando alguns dados de exemplo

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CORES = ["b", "g", "r", "c", "m", "y", "k", "w"]
TITLE =  ["Tensão x Corrente", "log(V) x Corrente"]

files = [
    os.path.dirname(__file__) + r"\..\dados\4\curvaVxI_diodo.csv",
    os.path.dirname(__file__) + r"\..\dados\4\curvaVxI_diodo.csv",
]

img_dir = os.path.dirname(__file__) + r"\\..\\images\\VxI_INCAND\\"
os.makedirs(img_dir, exist_ok=True)

fig, sub = plt.subplots(1, 2, figsize=(18, 6))

def parse_data(data:str):
    I = []
    V = []
    
    for line in data.strip().splitlines()[1:]:
        V.append(float(line.split(";")[0]))
        I.append(float(line.split(";")[1]))
        
    return V, I


for i, (file, title) in enumerate(zip(files, TITLE)):
    with open(file) as data:
        V, I = parse_data(data.read())
        sub[i].plot(V, I, color=CORES[i], alpha=0.6)
    
    if("log" in title):
        sub[i].set_xscale('log')
        
    sub[i].grid(True, linestyle="--", alpha=0.6, color="gray")
    sub[i].set_title(title)
    sub[i].set_xlabel('Eixo X')
    sub[i].set_ylabel('Eixo Y')

fig.savefig(img_dir + r"\\" + f"{len(os.listdir(img_dir))}.png")