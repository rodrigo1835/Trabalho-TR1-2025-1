from CamadaFisica.modulacao_banda_base import *
from CamadaFisica.modulacao_portadora import *
from CamadaDeEnlace.enquadramento import *
from CamadaDeEnlace.paridade import bit_paridade
from CamadaDeEnlace.crc import div_crc
from utils.graficos import grafico_banda_base, grafico_portadora
from utils.conversor import frase_para_bits
from utils.config import *

mensagem = input("Sua mensagem: ")
bit_mensagem = frase_para_bits(mensagem)

mensagem_erro = div_crc(bit_mensagem)
mensagem_enquadrada = contagem_de_quadros(mensagem_erro)
print(mensagem_erro)
print(mensagem_enquadrada)


'''
x = list(range(len(mensagem_modulada)))
y = mensagem_modulada
grafico_banda_base(x,y, MANCHESTER)

sinal_ask = ask(bit_mensagem, FREQ0, AMPLITUDE, BITRATE)
sinal_fsk = fsk(bit_mensagem, FREQ0, FREQ1, AMPLITUDE, BITRATE)
sinal_qam8 = qam8(bit_mensagem, FREQ0, AMPLITUDE, BITRATE)

grafico_portadora(bit_mensagem, BITRATE, sinal_ask, ASK)
grafico_portadora(bit_mensagem, BITRATE, sinal_fsk, FSK)
grafico_portadora(bit_mensagem, BITRATE, sinal_qam8, QAM8)

bits = "010111"
x = list(range(len(nrz_polar(bits))))
y = nrz_polar(bits)
grafico_banda_base(x, y, "NRZ_Polar")
'''