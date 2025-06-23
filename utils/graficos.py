import matplotlib.pyplot as plt
import numpy as np
from utils.config import *

def configurar_grafico_banda_base(titulo, x, y , cor):
    plt.figure(titulo)
    plt.step(x, y, where='post', color = cor)
    plt.title(titulo)
    plt.xlabel("Tempo")
    plt.ylabel("Nível de Sinal")
    plt.grid(True)

# Plotar Grafico da modulação banda base
def grafico_banda_base(x, y, modulacao):
    if(modulacao == "NRZ_Polar"):
        # NRZ-P
        configurar_grafico_banda_base(modulacao, x, y, "green")

    elif(modulacao == "Manchester"):
        # Manchester
        configurar_grafico_banda_base(modulacao, x, y, "blue")

    elif(modulacao == "Bipolar"):
        # Bipolar
        configurar_grafico_banda_base(modulacao, x, y, "red")

    else:
        print("Modulação não conhecida!")

    plt.show()


def configurar_grafico_portadora(titulo, x, y , cor):
    plt.figure(titulo)
    plt.plot(x, y, color = cor)
    plt.title(titulo)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.grid(True)

# Plotar Grafico da modulação Analogica
def grafico_portadora(bits, bitrate, sinal, modulacao):
    t_bit = 1 / bitrate

    # tempo total = quantidade de bits×duração de cada bit
    # Cada bit tem duração de t_bit = 1 / bitrate
    # Se bitrate = 1000, então cada bit dura 1ms
    # Se eu tenho 8 bits(1 byte) a transmissão dura 8 * t_bit = 8 * 0,001 = 0,008ms

    x = np.linspace(0, len(bits) * t_bit, len(sinal), endpoint=False)

    if(modulacao == "ASK"):
        # ASK
        configurar_grafico_portadora(modulacao, x, sinal, "green")

    elif(modulacao == "FSK"):
        # FSK
        configurar_grafico_portadora(modulacao, x, sinal, "blue")

    elif(modulacao == "8-QAM"):
        # 8-Qam
        configurar_grafico_portadora(modulacao, x, sinal, "purple")

    else:
        print("Modulação não conhecida!")

    plt.show()