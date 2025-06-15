import matplotlib.pyplot as plt
import numpy as np

# Modulação  NRZ-Polar
def nrz_polar(bits):
    v = 2
    nrz_p = []
    for bit in bits:
        amp = v / 2
        if bit == '1':
            nrz_p.append(amp)
        else:
            nrz_p.append(-amp)
    
    return nrz_p

# Modulação  Manchester            
def manchester(bits):
    v = 2
    manch = []
    
    for bit in bits:
        amp = v / 2
        if bit == '1':
            manch.append(-amp)
            manch.append(amp)
        else:
            manch.append(amp)
            manch.append(-amp)
          
    return manch

# Modulação  Bipolar
def bipolar(bits):
    v = 2
    bipo = []
    sinal = False
    
    
    for bit in bits:
        #Verifica se o bit anterior era = 1
        if bit == '1' and sinal:
            bipo.append(-v)
            sinal = False
        
        #Verifica se o bit anterior era != 1
        elif bit == '1' and not sinal:
            bipo.append(v)
            sinal = True
        
        #Se o bit anterior for 0, continua 0
        else:
            bipo.append(0)
    
    return bipo

def configurar_grafico_digital(titulo, x, y , cor):
    plt.figure(titulo)
    plt.step(x, y, where='post', color = cor)
    plt.title(titulo)
    plt.xlabel("Tempo")
    plt.ylabel("Nível de Sinal")
    plt.grid(True)

# Plotar Grafico da modulação banda base
def grafico_digital(bits):

    x0 = list(range(len(nrz_polar(bits))))
    y0 = nrz_polar(bits)

    x1 = list(range(len(manchester(bits))))
    y1 = manchester(bits)

    x2 = list(range(len(bipolar(bits))))
    y2 = bipolar(bits)

    # NRZ-P
    configurar_grafico_digital("NRZ-Polar", x0, y0, "green")

    # Manchester
    configurar_grafico_digital("Manchester", x1, y1, "blue")

    # Bipolar
    configurar_grafico_digital("Bipolar", x2, y2, "red")

    plt.show()


grafico_digital("101")