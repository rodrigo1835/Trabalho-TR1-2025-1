import socket
from utils.conversor import frase_para_bits
from Interface.transmissor_interface import get_dados_interface
from CamadaDeEnlace.paridade import bit_paridade
from CamadaDeEnlace.crc import crc
from CamadaDeEnlace.hamming import hamming
from CamadaDeEnlace.enquadramento import *
from CamadaFisica.modulacao_banda_base import *

def transmissor(mensagem, info):

    if not info:
        print("Nenhum dado foi coletado")
        return    
    mensagem = frase_para_bits(mensagem)

    match info["deteccao_correcao"]:
        case "Paridade":
            mensagem_erro = bit_paridade(mensagem)
        case "Crc-32":
            mensagem_erro = crc(mensagem)
        case "Hamming":
            mensagem_erro = hamming(mensagem)

    match info["enquadramento"]:
        case "Contagem De Quadros":
            mensagem_enquadrada = contagem_de_quadros(mensagem_erro)
        case "Flags com Inserção de Caracteres":
            mensagem_enquadrada = flags_com_insercao_bytes(mensagem_erro)
        case "Flags com Inserção de bits":
            mensagem_enquadrada = flags_com_insercao_bits(mensagem_erro)

    match info["modulacao_digital"]:
        case "NRZ_Polar":
            mensagem_modulada = nrz_polar(mensagem_enquadrada)
        
        case "Manchester":
            mensagem_modulada = manchester(mensagem_enquadrada)
        
        case "Bipolar":
            mensagem_modulada = bipolar(mensagem_enquadrada)

    print(f'''
            Mensagem em bits = {mensagem}
            Detecção/Correção = {mensagem_erro}
            Enquadramento = {mensagem_enquadrada}
            Modulação Digital = {mensagem_modulada}
          ''')
    return mensagem_modulada

def enviar(dados):
    # Converte para string o vetor da modulação
    mensagem = ','.join(str(b) for b in dados)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    client.send(mensagem.encode())
    client.close()
