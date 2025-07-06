def contagem_de_quadros(mensagem):
    # Adiciona um cabeçalho de 16 bits com o tamanho em bytes ao quadro.
    m = bin(len(mensagem) // 8)

    nova_mensagem = m[2:].zfill(16) + mensagem
    return nova_mensagem

def flags_com_insercao_bytes(mensagem):
    nova_mensagem = ""
    for i in range(0, len(mensagem), 8):
        byte = mensagem[i:i+8]
        
        if byte == "01000000":
            nova_mensagem += "0010111101000000"
        else:
            nova_mensagem += byte
    nova_mensagem = "01000000" + nova_mensagem + "01000000"
    
    return nova_mensagem

def flags_com_insercao_bits(mensagem):
    novaMensagem = ""
    qtd_uns = 0

    for i in range(len(mensagem)):
        bit = mensagem[i]
        novaMensagem += bit

        if bit == "1":
            qtd_uns += 1
            if qtd_uns == 5:
                # Só insere o 0 se o próximo bit for 1 (evita remover 0 legítimo)
                if i + 1 < len(mensagem) and mensagem[i + 1] == "1":
                    novaMensagem += "0"
                qtd_uns = 0
        else:
            qtd_uns = 0

    return "01111110" + novaMensagem + "01111110"




