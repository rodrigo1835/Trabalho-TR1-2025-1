import math

haming = ["P1","P2","M3","P4","M5","M6","M7","P8","M9","M10","M11"]
posi = [1,2,4,8]

def calc_paridade(palavra, pos_paridade):        
    dic_paridade = {}
    
    temp_palavra = palavra[:]
    
    for pos in pos_paridade:
        paridade = []
        i = pos - 1
        while i < len(palavra):
            bloco = palavra[i:i + pos]
            paridade += bloco
            i += 2 * pos  # Pula o próximo bloco do mesmo tamanho
        #print(f"Paridade na posição {pos}: {paridade}")
        temp_palavra[pos - 1] = sum(paridade) % 2
        
    return temp_palavra

def hamming(mensagem):
    d = len(mensagem)
    r = 0
    
    # Calcula o número de bits de paridade
    while (2 ** r) < (r + d + 1):
        r += 1

    tamanho_total = d + r
    nova_palavra = [0] * tamanho_total

    pos_paridade = []
    j = 0  # índice da mensagem original
    for i in range(1, tamanho_total + 1): # log(i = 0) dá ruim então começamos em i = 1
        if math.log2(i).is_integer():  # posição de paridade (2^i)
            nova_palavra[i - 1] = 0
            pos_paridade.append(i) # Colocar no vetor as posições dos bits de paridade
        else:
            nova_palavra[i - 1] = int(mensagem[j])
            j += 1
    
    
    palavra_final = calc_paridade(nova_palavra, pos_paridade)
    
    return palavra_final, nova_palavra


# Entradas
dados_bits = ["010", "111", "001", "1010", "0001"]
palavra_ham,nova_palavra = hamming(dados_bits[0])
print(palavra_ham, nova_palavra)
