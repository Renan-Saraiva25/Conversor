import tkinter as tk
from tkinter import ttk
import requests

# Dicionário de moedas
MOEDAS = {
    "Dólar Americano (USD)": "USD",
    "Euro (EUR)": "EUR",
    "Iene Japonês (JPY)": "JPY",
    "Peso Argentino (ARS)": "ARS",
    "Real Brasileiro (BRL)": "BRL"
}

# Função para obter a taxa de câmbio
def obter_taxa(origem, destino):
    url = f"https://v6.exchangerate-api.com/v6/7906388f71dfde8c2b489a8f/latest/{origem}"
    resposta = requests.get(url)
    dados = resposta.json()
    if resposta.status_code == 200 and dados["result"] == "success":
        return dados["conversion_rates"][destino]
    else:
        return None

# Função para realizar a conversão
def converter():
    try:
        valor = float(entrada_valor.get())
        moeda_origem = MOEDAS[combo_origem.get()]
        moeda_destino = MOEDAS[combo_destino.get()]
        taxa = obter_taxa(moeda_origem, moeda_destino)
        if taxa:
            resultado = valor * taxa
            label_resultado.config(
                text=f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}",
                fg="#ffd700"  # dourado
            )
        else:
            label_resultado.config(text="Erro ao buscar taxa. Verifique sua chave ou conexão.", fg="red")
    except ValueError:
        label_resultado.config(text="Digite um valor válido.", fg="red")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.geometry("450x320")
janela.configure(bg="#1b5e20")  # verde escuro

# Estilos de cor e fonte
cor_fundo = "#1b5e20"
cor_botao = "#66bb6a"  # verde claro
cor_dourado = "#ffd700"
cor_texto = "#ffffff"

estilo_label = {"font": ("Arial", 12), "bg": cor_fundo, "fg": cor_texto}
estilo_entry = {"font": ("Arial", 12), "bg": "#ffffff", "fg": "#000000"}
estilo_combo = {"font": ("Arial", 11)}

# Título
tk.Label(janela, text="Conversor de Moedas", font=("Arial", 16, "bold"),
         bg=cor_fundo, fg=cor_dourado).pack(pady=10)

# Entrada do valor
tk.Label(janela, text="Valor:", **estilo_label).pack()
entrada_valor = tk.Entry(janela, **estilo_entry, justify="center")
entrada_valor.pack(pady=5)

# Moeda de origem
tk.Label(janela, text="De:", **estilo_label).pack()
combo_origem = ttk.Combobox(janela, values=list(MOEDAS.keys()), font=("Arial", 11))
combo_origem.current(0)
combo_origem.pack(pady=5)

# Moeda de destino
tk.Label(janela, text="Para:", **estilo_label).pack()
combo_destino = ttk.Combobox(janela, values=list(MOEDAS.keys()), font=("Arial", 11))
combo_destino.current(1)
combo_destino.pack(pady=5)

# Botão de conversão
botao_converter = tk.Button(
    janela,
    text="Converter",
    command=converter,
    bg=cor_botao,
    fg="#000000",
    font=("Arial", 12, "bold"),
    relief="raised",
    padx=10,
    pady=5
)
botao_converter.pack(pady=15)

# Resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 12, "bold"),
                           bg=cor_fundo, fg=cor_dourado)
label_resultado.pack()

janela.mainloop()
