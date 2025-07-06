import threading
from Interface.receptor_interface import criar_interface_receptor
from Interface.transmissor_interface import criar_interface_transmissor, get_dados_interface
from Servidor.receptor import receber, receptor
from Servidor.transmissor import enviar, transmissor

recebido_var = None
erro_var = None

def iniciar_transmissor():
    janela_transmissor = criar_interface_transmissor()
    janela_transmissor.mainloop()

def iniciar_receptor():
    global janela_receptor, recebido_var, enquadramento_var, erro_var, modulacao_var

    janela_receptor, recebido_var, enquadramento_var, erro_var, modulacao_var = criar_interface_receptor()
    janela_receptor.mainloop()

def fluxo_comunicacao():
    transmissor_thread.join()
    mensagem, info = get_dados_interface()

    if not mensagem or not info:
        print("Dados Inválidos.")
        return

    # Inicia receptor socket primeiro se não da erro se inciar o transmissor primeiro
    def escutar():
        dados_recebidos = receber()
        receptor(dados_recebidos, info, recebido_var, erro_var, janela_receptor)

    receptor_socket_thread = threading.Thread(target=escutar)
    receptor_socket_thread.start()

    sinal = transmissor(mensagem, info)
    enviar(sinal)

    receptor_socket_thread.join()

transmissor_thread = threading.Thread(target=iniciar_transmissor)
receptor_thread = threading.Thread(target=iniciar_receptor)
fluxo_thread = threading.Thread(target=fluxo_comunicacao)

transmissor_thread.start()
receptor_thread.start()
fluxo_thread.start()
