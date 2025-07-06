def bit_paridade(mensagem):
    xor = 0
    for bit in mensagem:
        xor = int(bit) ^ xor

    mensagem_com_paridade = mensagem + str(xor)
    return mensagem_com_paridade

def verifica_paridade(mensagem):
    tamanho_mensagem = len(mensagem)
    paridade = int(mensagem[tamanho_mensagem - 1])

    xor = 0
    for i in range(0, tamanho_mensagem - 1):
        xor = int(mensagem[i]) ^ xor
    
    if(xor != paridade):
        return mensagem[:-1], "Com erro"
    
    return mensagem[:-1], "Sem erro"