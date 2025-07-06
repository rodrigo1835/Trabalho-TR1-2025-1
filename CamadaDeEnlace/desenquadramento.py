def desenquadra_quadros(mensagem, tipo_erro):
    mensagem = "".join(str(bit) for bit in mensagem)

    # Extrai os 16 primeiros bits (número de bytes originais)
    tamanho_mensagem_bytes = int(mensagem[:16], 2)
    print("Tamanho em bytes:", tamanho_mensagem_bytes)

    mensagem = mensagem[16:]  # Remove o cabeçalho

    tamanho_mensagem_bits = tamanho_mensagem_bytes * 8

    match tipo_erro:
        case "Paridade":
            bits_extra = 1
        case "Crc-32":
            bits_extra = 32
        case "Hamming":
            # Calcular número de bits totais para uma mensagem com Hamming
            d = tamanho_mensagem_bits
            r = 0
            while (2 ** r) < (r + d + 1):
                r += 1
            bits_extra = r
        case _:
            bits_extra = 0

    total_bits = tamanho_mensagem_bits + bits_extra

    mensagem_desenquadrada = mensagem[:total_bits]
    return mensagem_desenquadrada


def desenquadra_bytes(mensagem):
    mensagem = "".join(str(bit) for bit in mensagem)
    mensagem = mensagem[8:-8]  # Remove as flags 01000000 (assumindo que não houve erro de enquadramento)

    mensagem_desenquadrada = ""
    i = 0

    while i <= len(mensagem):
        byte = mensagem[i:i+8]

        if byte == "00101111":  # Byte de escape "/"
            proximo = mensagem[i+8:i+16]

            if proximo == "01000000":  # Escapando a flag '@'
                mensagem_desenquadrada += "01000000"
                i += 16  # pula o escape e o byte escapado
                continue
            elif proximo == "00101111":  # Escapando o próprio escape '/'
                mensagem_desenquadrada += "00101111"
                i += 16
                continue
            else:
                # Escape inválido ou corrompido: adiciona o byte normalmente
                mensagem_desenquadrada += byte
                i += 8
                continue

        else:
            mensagem_desenquadrada += byte
            i += 8

    print(f"Mensagem Desenquadrada: {mensagem_desenquadrada}")
    return mensagem_desenquadrada


def desenquadra_bits(mensagem):
    mensagem = "".join(str(bit) for bit in mensagem)

    # Remove as flags 01111110 do início e fim
    mensagem = mensagem[8:-8]

    mensagem_desenquadrada = ""
    qtd_uns = 0

    i = 0
    while i < len(mensagem):
        if(mensagem[i] == "1"):
            qtd_uns += 1
            mensagem_desenquadrada += mensagem[i]
            i += 1

            if(qtd_uns == 5):
                i += 1
                qtd_uns = 0
        else:
            mensagem_desenquadrada += mensagem[i]
            qtd_uns = 0
            i += 1

    return mensagem_desenquadrada


