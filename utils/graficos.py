import matplotlib.pyplot as plt
import numpy as np

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
