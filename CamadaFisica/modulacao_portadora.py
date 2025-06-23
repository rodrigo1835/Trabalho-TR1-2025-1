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
