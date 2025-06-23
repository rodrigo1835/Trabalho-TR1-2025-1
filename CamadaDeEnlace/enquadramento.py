def contagem_de_quadros(mensagem):
    # Adiciona um cabeçalho de 16 bits com o tamanho em bytes ao quadro.
    m = bin(len(mensagem) // 8)

    nova_mensagem = m[2:].zfill(16) + mensagem
    return nova_mensagem

def flags_com_insercao(mensagem):
    novaMensagem = ""
    for i in range(0, len(mensagem)):
        if mensagem[i] == "@":
            novaMensagem += "/@"
        else:
            novaMensagem += mensagem[i]
    novaMensagem = "@" + novaMensagem + "@"
        
    return novaMensagem

def flags_com_insercao_bits(mensagem):
    novaMensagem = "" 
    qtd_uns = 0

    for i in range(0, len(mensagem)):
        if(mensagem[i] == "1"):
            qtd_uns += 1
            if(qtd_uns == 5):
                novaMensagem += "0"
                qtd_uns = 0
            novaMensagem += mensagem[i]

        else:
            novaMensagem += mensagem[i]
        
    novaMensagem = "01111110" + novaMensagem + "01111110"

    return novaMensagem



