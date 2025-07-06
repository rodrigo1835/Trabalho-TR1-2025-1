import socket

from CamadaDeEnlace.crc import verifica_crc
from CamadaFisica.modulacao_portadora import *
from CamadaFisica.demodulacao_banda_base import *
from CamadaDeEnlace.desenquadramento import *
from CamadaDeEnlace.paridade import verifica_paridade
from CamadaDeEnlace.hamming import verificar_paridade_hamming
from utils.config import *
from utils.conversor import bits_para_frase
from utils.graficos import grafico_banda_base, grafico_portadora

def receptor(mensagem, info, recebidor_var, erro_var, janela_receptor):
    # Informações para o gráfico banda base
    x = list(range(len(mensagem)))
    y = mensagem
    match info["modulacao_digital"]:
        case "NRZ_Polar":
            mensagem_demodulada = demodula_nrz_polar(mensagem)

            grafico = grafico_banda_base(x,y, NRZ_P)

        case "Manchester":
            mensagem_demodulada = demodula_machester(mensagem)
        
            grafico = grafico_banda_base(x,y, MANCHESTER)

        case "Bipolar":
            mensagem_demodulada = demodula_bipolar(mensagem)

            grafico = grafico_banda_base(x,y, BIPOLAR)
    
    match info["grafico_portadora"]:
        case "ASK":
            sinal_ask = ask(mensagem_demodulada, FREQ0, AMPLITUDE, BITRATE)
            grafico_digital = grafico_portadora(mensagem_demodulada, BITRATE, sinal_ask, ASK)
        
        case "FSK":
            sinal_fsk = fsk(mensagem_demodulada, FREQ0, FREQ1, AMPLITUDE, BITRATE)
            grafico_digital = grafico_portadora(mensagem_demodulada, BITRATE, sinal_fsk, FSK)
        
        case "QAM-8":
            sinal_qam8 = qam8(mensagem_demodulada, FREQ0, AMPLITUDE, BITRATE)
            grafico_digital = grafico_portadora(mensagem_demodulada, BITRATE, sinal_qam8, QAM8)

    match info["enquadramento"]:
        case "Contagem De Quadros":
            mensagem_desenquadrada = desenquadra_quadros(mensagem_demodulada, info["deteccao_correcao"])
        case "Flags com Inserção de Caracteres":
            mensagem_desenquadrada = desenquadra_bytes(mensagem_demodulada)
        case "Flags com Inserção de bits":
            mensagem_desenquadrada = desenquadra_bits(mensagem_demodulada)

    match info["deteccao_correcao"]:
        case "Paridade":
            mensagem_erro, erro = verifica_paridade(mensagem_desenquadrada)
        case "Crc-32":
            mensagem_erro, erro = verifica_crc(mensagem_desenquadrada)
        case "Hamming":
            mensagem_erro, erro = verificar_paridade_hamming(mensagem_desenquadrada)
    
    mensagem_final = bits_para_frase(mensagem_erro)
    print(f'''
        Mensagem Recebida: {mensagem}
        Mensagem Demodulada: {mensagem_demodulada}
        Mensagem Desenquadrada: {mensagem_desenquadrada}
        Mensagem Detecção de Erro: {mensagem_erro}
        Mensagem Final: {mensagem_final}
        Erro: {"Sem erro" if erro else "Com Erro" }
    ''')
    
    def atualizar_interface():
        recebidor_var.set(mensagem_final)
        erro_var.set("Sem erro" if erro else "Com erro")

    janela_receptor.after(0, atualizar_interface)

    

def receber():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    conn, addr = server.accept()

    dados = conn.recv(4096).decode()
    conn.close()

    # Converte de volta para lista de inteiros
    vetor = [int(x) for x in dados.split(',')]
    return vetor
