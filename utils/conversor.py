import random

def frase_para_bits(frase):
    # Codifica a frase para bytes no formato utf-8
    bytes_frase = frase.encode("utf-8")
    
    # Converte cada byte para uma string binária de 8 bits
    bits = ''.join(format(byte, '08b') for byte in bytes_frase)

    return bits

def bits_para_frase(bits):
    bits = ''.join(str(bit) for bit in bits)
    mensagem = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        decimal = int(byte, 2) # De bits para decimal
        caractere = chr(decimal) # Decimal para caractere
        mensagem.append(caractere)
        
    return ''.join(mensagem)

def adicionar_ruido(bits, prob_erro = 0.01):
    bits_com_erro = []

    for bit in bits:
        if random.random() < prob_erro: # random.random gera um número entre 0 e 1
            if(bit == 1 or bit == -1):
                bit = 0
            else:
                bit = 1
        bits_com_erro.append(bit)
    
    return bits_com_erro