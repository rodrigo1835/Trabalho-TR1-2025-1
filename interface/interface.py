import tkinter as tk
from tkinter import ttk

fontePadrao = ("Helvetica", 10)

janela = tk.Tk()
janela.geometry("400x400")
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

checkbox = tk.Checkbutton(janela,
    text="Mostrar gráfico",
    font = fontePadrao,
    variable = mostrar)
checkbox.grid(row = 3, column = 0)

tk.Label(
    janela,
    text="Modulação Digital:"
).grid(row = 4, column=0, padx = 5, pady = 5, sticky=tk.E)

modulacaoDigital = ttk.Combobox(
    janela,
    values=["NRZ-P","Manchester", "BIPOLAR"],
    state="readonly"
)
modulacaoDigital.grid(row = 4, column=1, padx = 5, pady = 5)


tk.Label(
    janela,
    text="Modulação Analogica:"
).grid(row = 5, column=0, padx = 5, pady = 5, sticky=tk.E)
modulacaoAnalogica = ttk.Combobox(
    janela,
    values = ["PSK", "ASK", "8-QAM"],
    state = "readonly"
)
modulacaoAnalogica.grid(row = 5, column = 1, padx = 5, pady = 5)


tk.Label(
    janela,
    text="Enquadramento:"
).grid(row = 6, column=0, padx = 5, pady = 5, sticky=tk.E)
enquadramento = ttk.Combobox(
    janela,
    values = ["Contagem De Quadros", "Flags com Inserção"],
    state = "readonly"
)
enquadramento.grid(row = 6, column = 1, padx = 5, pady = 5)


tk.Label(
    janela,
    text="Detecção de Erros:"
).grid(row = 7, column=0, padx = 5, pady = 5, sticky=tk.E)
deteccao = ttk.Combobox(
    janela,
    values = ["Paridade"],
    state = "readonly"
)
deteccao.grid(row = 7, column = 1, padx = 5, pady = 5)

tk.Label(
    janela,
    text="Correção de Erros:"
).grid(row = 8, column=0, padx = 5, pady = 5, sticky=tk.E)
correcao = ttk.Combobox(
    janela,
    values = ["Hamming"],
    state = "readonly"
)
correcao.grid(row = 8, column = 1, padx = 5, pady = 5)


tk.Label(
    janela,
    text="Taxa de Erro:"
).grid(row = 9, column=0, padx = 5, pady = 5, sticky=tk.E)
taxaDeErros = tk.Scale(
    janela,
    from_ = 0, to = 100, orient = "horizontal"
)
taxaDeErros.grid(row = 9, column = 1, padx = 5, pady = 5)

botao = ttk.Button(janela, text="Transmitir")
botao.grid(row=10, column=0, columnspan=2, padx=5, pady=15, sticky="ew")

janela.mainloop()
