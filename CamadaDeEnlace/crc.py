import zlib

'''
O CRC-32 IEEE 802.3 usa:
 - Polinômio refletido: 0xEDB88320 (inverso de 0x04C11DB7)
 - Entrada e saída refletidas
 - Valor inicial: 0xFFFFFFFF
 - Pós-processamento: inverte todos os bits no final (complemento de 1)
'''

# Polinômio padrão do CRC-32 (forma normal, não refletida)
polinomio = "100000100110000010001110110110111"  # 0x04C11DB7

# EDC (Error Detection Code) inicial: (tamanho do polinomio - 1) bit
EDC = "1" * (len(polinomio) - 1)

def confere_bytes(string):
    """
    Garante que a string tenha múltiplos de 8 bits (1 byte).
    Preenche com zeros à esquerda, se necessário.
    """
    while(len(string) % 8 != 0):
        string = "0" + string
    return string

def reflete_bit(bits):
    """
    Reflete os bits (espelhamento da string binária).
    """
    return bits[::-1]

def xor(a, b):
    """
    Operação XOR bit a bit entre duas strings binárias de mesmo tamanho.
    """
    xor = ""
    for i in range(len(a)):
        xor += str(int(a[i]) ^ int(b[i]))
    return xor

def div_crc(dividendo, divisor = polinomio):
    """
    Executa a divisão polinomial em módulo 2 (sem transporte) para cálculo do CRC.
    Retorna o resto da divisão, que é o CRC bruto.
    """
    dividendo = dividendo + EDC
    divisor_len = len(divisor)
    dividendo_temp = dividendo[:divisor_len]
    resto_dividendo = dividendo[divisor_len:]

    while len(resto_dividendo) > 0:
        if dividendo_temp[0] == "1":
            dividendo_temp = xor(dividendo_temp, divisor)
        else:
            dividendo_temp = xor(dividendo_temp, "0" * divisor_len)

        dividendo_temp = dividendo_temp[1:] + resto_dividendo[0]
        resto_dividendo = resto_dividendo[1:]

    # Última etapa da divisão
    if dividendo_temp[0] == "1":
        dividendo_temp = xor(dividendo_temp, divisor)
    else:
        dividendo_temp = xor(dividendo_temp, "0" * divisor_len)

    return dividendo_temp[1:]  # Retorna o CRC (resto), descartando o bit mais significativo


'''
# =======================
# Processamento principal
# =======================

# 1. Mensagem original (em bits)
mensagem = "111000"

# 2. Garante que a mensagem tenha múltiplos de 8 bits
mensagem = confere_bytes(mensagem)

# 3. Reflete os bits da mensagem (bitwise reverse)
mensagem_refletida = reflete_bit(mensagem)

# 4. Adiciona os 32 bits do EDC à mensagem refletida
mensagem_com_edc = mensagem_refletida + EDC

# 5. Calcula o CRC bruto usando divisão polinomial
crc = div_crc(mensagem_com_edc, polinomio)

# 6. Reflete os bits do CRC e faz complemento de 1 (inversão de bits)
crc_refletido = reflete_bit(crc)
crc_final = xor(crc_refletido, "1" * len(crc_refletido))

# ========================
# Verificação no receptor
# ========================

# 7. Simula o receptor revertendo o pós-processamento
crc_recebido = reflete_bit(crc_final)
crc_corrigido = xor(crc_recebido, "1" * len(crc_recebido))

# 8. Junta a mensagem com o CRC e verifica o resto da divisão (deve ser zero)
mensagem_crc_corrigido = mensagem_refletida + crc_corrigido
verificacao = div_crc(mensagem_crc_corrigido, polinomio)

# ================
# Exibição dos dados
# ================

print("Mensagem original:             ", mensagem)
print("Mensagem refletida:            ", mensagem_refletida)
print("CRC bruto:                     ", crc)
print("CRC refletido + complemento:   ", crc_final)
print("Verificação CRC no receptor:   ", verificacao)
'''