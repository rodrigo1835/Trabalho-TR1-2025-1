import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def executar():
    global info
    global mensagem
    mensagem = entrada.get()
    modulacao_digital = modulacaoDigital.get()
    grafico_portadora = modulacaoAnalogica.get()
    quadro = enquadramento.get()
    detecta_corrige = deteccao.get()

    if not mensagem:
        messagebox.showwarning("Digite um mensagem")
        return
    
    try:
        info = {
            "modulacao_digital": modulacao_digital,
            "grafico_portadora": grafico_portadora,
            "enquadramento": quadro,
            "deteccao_correcao": detecta_corrige
        }
        print("teste")
        janela.destroy()
    
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {e}")

def get_dados_interface():
    return mensagem, info

def criar_interface_transmissor():

    global janela, entrada, modulacaoDigital, modulacaoAnalogica, enquadramento, deteccao
    fontePadrao = ("Helvetica", 10)

    janela = tk.Tk()
    janela.geometry("400x300")
    janela.title("Simulador")
    janela.columnconfigure(0, weight=1)
    janela.columnconfigure(1, weight=1)

    tk.Label(
        janela,
        font = ("Helvetica", 14, "bold"),
        text = "Transmissor"
    ).grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

    # Campo de Texto
    tk.Label(
        janela,
        font = fontePadrao,
        text = "Texto de entrada:"
    ).grid(row = 1, column=0, padx=5 , pady = 5, sticky=tk.E)
    entrada = ttk.Entry(janela)
    entrada.grid(row = 1, column = 1, padx = 5, pady = 5)

    mostrar = tk.IntVar()
    '''
    checkbox = tk.Checkbutton(janela,
        text="Mostrar gráfico",
        font = fontePadrao,
        variable = mostrar)
    checkbox.grid(row = 3, column = 0)
    '''

    tk.Label(
        janela,
        text="Modulação Digital:"
    ).grid(row = 4, column=0, padx = 5, pady = 5, sticky=tk.E)

    modulacaoDigital = ttk.Combobox(
        janela,
        values=["NRZ_Polar","Manchester", "Bipolar"],
        state="readonly"
    )
    modulacaoDigital.grid(row = 4, column=1, padx = 5, pady = 5)
    modulacaoDigital.current(0)

    tk.Label(
        janela,
        text="Gráfico Modulação Analogica:"
    ).grid(row = 5, column=0, padx = 5, pady = 5, sticky=tk.E)
    modulacaoAnalogica = ttk.Combobox(
        janela,
        values = ["FSK", "ASK", "QAM-8"],
        state = "readonly"
    )
    modulacaoAnalogica.grid(row = 5, column = 1, padx = 5, pady = 5)
    modulacaoAnalogica.current(0)

    tk.Label(
        janela,
        text="Enquadramento:"
    ).grid(row = 6, column=0, padx = 5, pady = 5, sticky=tk.E)
    enquadramento = ttk.Combobox(
        janela,
        values = ["Contagem De Quadros", "Flags com Inserção de Caracteres", "Flags com Inserção de bits"],
        state = "readonly"
    )
    enquadramento.grid(row = 6, column = 1, padx = 5, pady = 5)
    enquadramento.current(0)

    tk.Label(
        janela,
        text="Detecção/Correção de Erros:"
    ).grid(row = 7, column=0, padx = 5, pady = 5, sticky=tk.E)
    deteccao = ttk.Combobox(
        janela,
        values = ["Paridade", "Crc-32", "Hamming"],
        state = "readonly"
    )
    deteccao.grid(row = 7, column = 1, padx = 5, pady = 5)
    deteccao.current(0)

    botao = ttk.Button(janela, text="Transmitir", command=executar)
    botao.grid(row=10, column=0, columnspan=2, padx=5, pady=15, sticky="ew")

    return janela
