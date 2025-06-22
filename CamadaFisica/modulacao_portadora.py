import math
import matplotlib.pyplot as plt
import numpy as np


def ask(bits, freq, amp, bitrate):
    #Se cada bit dura 1 ms (bitrate = 1000 bps), e sua taxa de amostragem for 100 kHz, você precisa de:
    #100 amostras por bit (100 mil amostras/seg ÷ 1000 bits/seg)
    #Então para 8 bits → 8 x 100 = 800 amostras no total.
    
    fs = 100 * freq # Taxa de amostragem
    t_bit = 1 / bitrate # Duração de um bit em segundos
    amostras_por_bit = int(fs * t_bit)

    tempo = np.linspace(0, t_bit, amostras_por_bit, endpoint=False) # Gera um vetor de 0 a quantidade de amostras
    
    sinal = []
    for bit in bits:
        if bit == '1':
            for t in tempo:
                # sinal(t) = A.Sen(2πft)
                sinal.append(amp * math.sin(2 * math.pi * freq * t))
        else:
            for t in tempo:
                sinal.append(0)

    return sinal

def fsk(bits, freq0, freq1, amp, bitrate):
    fs = 100 * max(freq0, freq1) # Taxa de amostragem
    t_bit = 1 / bitrate # Duração de um bit em segundos
    amostras_por_bit = int(fs * t_bit)

    tempo = np.linspace(0, t_bit, amostras_por_bit, endpoint=False) # Gera um vetor de 0 a quantidade de amostras
    
    sinal = []
    for bit in bits:
        if bit == '1':
            for t in tempo:
                # sinal(t) = A.Sen(2πft)
                sinal.append(amp * math.sin(2 * math.pi * freq0 * t))
        else:
            for t in tempo:
                sinal.append(amp * math.sin(2 * math.pi * freq1 * t))

    return sinal

def qam8(bits, freq0, amp, bitrate) :
    costelacao = {"000": (1,1), "001": (1,-1), "010": (-1,1), "011": (-1,-1), "100": (math.sqrt(2), 0), "101": (-math.sqrt(2), 0), "110": (0, math.sqrt(2)), "111": (0, -math.sqrt(2))}

    fs = 10 * freq0 # Taxa de amostragem
    t_bit = 1 / bitrate # Duração de um bit em segundos
    t_simbolo = t_bit * 3
    amostras_por_simbolo = int(fs * t_simbolo)

    tempo = np.linspace(0, t_simbolo, amostras_por_simbolo, endpoint=False) # Gera um vetor de 0 a quantidade de amostras
    
    # Verificar se o simbolo é multiplo de 3 se não for adiciona 0 a direita
    while( (len(bits) % 3) != 0 ):
        bits += "0"

    sinal = []
    for i in range(0, len(bits), 3):
        agrupamento_bits = bits[i:i+3]
        simbolo = costelacao[agrupamento_bits]
        for t in tempo:
            I, Q = simbolo
            s = I * math.cos(2 * math.pi * freq0 * t) + Q * math.sin(2 * math.pi * freq0 * t)
            sinal.append(s)

    return sinal

def configurar_grafico_analogico(titulo, x, y , cor):
    plt.figure(titulo)
    plt.plot(x, y, color = cor)
    plt.title(titulo)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.grid(True)

# Plotar Grafico da modulação Analogica
def grafico_analogico():
    #bits = "0101000001001010111010101010101"
    bits = "010001010111010100100000011000010111"

    bitrate = 1000
    freq0 = 2 * 10 ** 3
    freq1 = 8 * 10 ** 3
    t_bit = 1 / bitrate
    sinal0 = ask(bits, freq0, 1, bitrate)
    sinal1 = fsk(bits, freq0 , freq1, 1, bitrate)
    sinal2 = qam8(bits, freq0, 1, bitrate)

    # tempo total = quantidade de bits×duração de cada bit
    # Cada bit tem duração de t_bit = 1 / bitrate
    # Se bitrate = 1000, então cada bit dura 1ms
    # Se eu tenho 8 bits(1 byte) a transmissão dura 8 * t_bit = 8 * 0,001 = 0,008ms

    x0 = np.linspace(0, len(bits) * t_bit, len(sinal0), endpoint=False)
    y0 = sinal0

    x1 = np.linspace(0, len(bits) * t_bit, len(sinal1), endpoint=False)
    y1 = sinal1

    x2 = np.linspace(0, len(bits) * t_bit, len(sinal2), endpoint=False)
    y2 = sinal2

    # ASK
    configurar_grafico_analogico("ASK", x0, y0, "green")

    # PSK
    configurar_grafico_analogico("PSK", x1, y1, "blue")

    # 8-Qam
    configurar_grafico_analogico("8-QAM", x2, y2, "purple")

    plt.show()

grafico_analogico()