def frase_para_bits(frase):
    # Codifica a frase para bytes no formato utf-8
    bytes_frase = frase.encode("utf-8")
    
    # Converte cada byte para uma string binária de 8 bits
    bits = ''.join(format(byte, '08b') for byte in bytes_frase)

    return bits