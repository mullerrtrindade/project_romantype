# Imports 

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Conversor de Números para Algarismos Romanos 

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 
        1
    ]
    syms = ["M", "CM", "D", "CD", "C",
            "XC", "L", "XL", "X",
            "IX", "V", "IV",
            "I"]
    
    roman = ""
    for i in range(len(val)):
        count = num // val[i]
        roman += syms[i] * count
        num -= val[i] * count
    return roman
# Funções de interface gráfica

def converter():
    entrada = campo_numero.get().strip()

    try: 
        numero = int(entrada)
        if numero < 1 or numero > 3999:
            resultado_var.set("---")
            mensagem_var.set("Por favor, digite um número inteiro entre 1 e 3999."
            )
            mensagem_label.configure(bootstyle="danger")
        else:
            roman_numeral = int_to_roman(numero)
            resultado_var.set(roman_numeral)
            mensagem_var.set("Conversão realizada com sucesso!")
            mensagem_label.configure(bootstyle="success")
    except ValueError:
        resultado_var.set("---")
        mensagem_var.set("Erro: Por favor, digite um número inteiro válido.")
        mensagem_label.configure(bootstyle="danger")
# Janela Principal 
janela = ttk.Window(

    title="Conversor de Números para Algarismos Romanos",
    themename="darkly",
)
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

largura = int(largura_tela * 0.4)
altura = int(altura_tela * 0.4)

janela.geometry(f"{largura}x{altura}+{(largura_tela - largura) // 2}+{(altura_tela - altura) // 2}")

titulo = ttk.Label(janela, text="Conversor de Números para Algarismos Romanos", 
                   font=("Helvetica", 16))
titulo.pack(pady=(20, 15))

campo_numero = ttk.Entry(
    janela,
    font=("Helvetica", 14),
    justify="center",
    width=20
)
campo_numero.pack(pady=10)

botao_converter = ttk.Button(
    janela,
    text="Converter",
    command=converter,
    bootstyle="primary",
)
botao_converter.pack(pady=10)

resultado_var = ttk.StringVar(value="---")
resultado_label = ttk.Label(
    janela,
    textvariable=resultado_var,
    font=("Helvetica", 24, "bold"),
    bootstyle="info",
)
resultado_label.pack(pady=15)

mensagem_var = ttk.StringVar(value="")
mensagem_label = ttk.Label(
    janela,
    textvariable=mensagem_var,
    font=("Helvetica", 12),
    bootstyle="secondary",
)
mensagem_label.pack(pady=10)

campo_numero.focus()
janela.bind("<Return>", lambda event: converter())


mensagem_var.set("Insira um número inteiro entre 1 e 3999 e pressione \"Converter\".")
mensagem_label.configure(bootstyle="info")


janela.mainloop()
