import tkinter as tk
from tkinter import ttk

def criar_interface_receptor():
    fontePadrao = ("Helvetica", 10)

    janela = tk.Tk()
    janela.geometry("400x300")
    janela.title("Simulador")
    janela.columnconfigure(0, weight=1)
    janela.columnconfigure(1, weight=1)

    recebido_var = tk.StringVar()
    enquadramento_var = tk.StringVar()
    erro_var = tk.StringVar()
    modulacao_var = tk.StringVar()

    tk.Label(
        janela,
        font = ("Helvetica", 14, "bold"),
        text = "Receptor"
    ).grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

    # Campo de Texto
    tk.Label(
        janela,
        font = fontePadrao,
        text = "Texto Recebido:"
    ).grid(row = 1, column=0, padx=5 , pady = 5, sticky=tk.E)
    recebido = ttk.Label(janela, textvariable = recebido_var)
    recebido.grid(row = 1, column = 1, padx = 5, pady = 5)

    tk.Label(
        janela,
        text="Houve erro?"
    ).grid(row = 2, column=0, padx = 5, pady = 5, sticky=tk.E)
    erro = ttk.Label(janela, textvariable=erro_var)
    erro.grid(row = 2, column=1, padx = 5, pady = 5)
    
    tk.Label(
        janela,
        text = "Mostrar Gráfico"
    ).grid(row = 3, column=0, padx = 5, pady = 5, sticky=tk.E)
    grafico = ttk.Button(janela, command=lambda: print("Gráfico aqui"))
    grafico.grid(row = 3, column=1, padx = 5, pady = 5)

    return janela, recebido_var, enquadramento_var, erro_var, modulacao_var
