from CamadaFisica.modulacao_banda_base import *
from CamadaDeEnlace.paridade import bit_paridade
from CamadaDeEnlace.enquadramento import *
from utils.graficos import grafico_banda_base 
from utils.conversor import frase_para_bits

EDC = "00000000000000000000000000000000"
mensagem = input("Sua mensagem: ")
print(f"mensagem original: {mensagem}")

bit_mensagem = frase_para_bits(mensagem)
print(f"mensagem em bits: {bit_mensagem}")

bit_mensagem_edc = bit_mensagem + EDC

mensagem_com_controle_de_erro = bit_paridade(bit_mensagem)
print(f"mensagem com controle de erro: {mensagem_com_controle_de_erro}")

mensagem_modulada = nrz_polar(mensagem_com_controle_de_erro)
print(f"mensagem modulada: {mensagem_modulada}")

mensagem_enquadrada = contagem_de_quadros(mensagem_modulada)
print(f"mensagem enquadrada: {mensagem_enquadrada}")

'''
bits = "010111"
x = list(range(len(nrz_polar(bits))))
y = nrz_polar(bits)
grafico_banda_base(x, y, "NRZ_Polar")
'''