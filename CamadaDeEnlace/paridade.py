def bit_paridade(mensagem):
    xor = 0
    for bit in mensagem:
        xor = int(bit) ^ xor

    mensagem_com_paridade = mensagem + str(xor)
    return mensagem_com_paridade
