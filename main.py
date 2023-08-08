import random
import tkinter as tk
from tkinter import messagebox

global resultado_var

def escolher_skin():
    return random.choice(skins)

def escolher_papel():
    return random.choice(papeis)

def rolar_novamente():
    global resultado_var

    skin_escolhida = escolher_skin()
    papel_escolhido = escolher_papel()

    resultado_var.set(f"A skin escolhida é: {skin_escolhida}\nVocê fará build: {papel_escolhido}")

def sair():
    root.destroy()

skins = [
    "Nunu Base",
    "Nunu Pé-Grande",
    "Nunu Natalinos",
    "Nunu Bicho-Papão",
    "Nunu Robótico",
    "Nunu Demolidor",
    "Nunu TPA",
    "Nunu Zumbi (Famoso bola de catarro)",
    "Nunu de Papel",
    "Nunu Embalos no Espaço",
    "Nunu e Mellump"
]

papeis = ["AP", "Tank"]

root = tk.Tk()
root.title("Escolha de Skin e Build")

# Define o tamanho da janela para 400x400
root.geometry("800x500")

# Centraliza a janela no monitor
largura_janela = 800
altura_janela = 500
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
x_pos = (largura_tela - largura_janela) // 2
y_pos = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

# Inicializa a variável resultado_var
resultado_var = tk.StringVar()

# Rola a opção aleatoriamente
rolar_novamente()

# Define a fonte para o rótulo de resultado
fonte_resultado = ("Helvetica", 14)

# Cria o rótulo para exibir o resultado
resultado_label = tk.Label(root, textvariable=resultado_var, justify="center", font=fonte_resultado)
resultado_label.pack(pady=10)

# Define a fonte para os botões
fonte_botoes = ("Helvetica", 12)

# Cria o botão "Rolar Novamente"
rolar_button = tk.Button(root, text="Rolar Novamente", command=rolar_novamente, font=fonte_botoes, height=2)
rolar_button.pack()

# Cria o botão "Sair"
sair_button = tk.Button(root, text="Sair", command=sair, font=fonte_botoes, height=2)
sair_button.pack()

# Adiciona um espaço para a mensagem "Discord"
espaco_discord_label = tk.Label(root, text="", font=("Helvetica", 10))
espaco_discord_label.pack()

# Define a fonte para o bottom
fonte_bottom = ("Helvetica", 10, "italic")

# Adiciona uma mensagem "Discord" na parte inferior
discord_label = tk.Label(root, text="Discord: rropelato", justify="center", font=(fonte_bottom))
discord_label.pack(side="bottom", pady=10)

# Adiciona uma mensagem "Github" na parte inferior
github_label = tk.Label(root, text="Github: Ropelatoo", justify="center", font=(fonte_bottom))
github_label.pack(side="bottom", pady=10)

# Adiciona uma mensagem "Criado por Ropelato" na parte inferior
criado_por_label = tk.Label(root, text="Criado por Ropelato", justify="center", font=(fonte_bottom))
criado_por_label.pack(side="bottom", pady=10)

# Adiciona uma mensagem "Mensagem" na parte inferior
mensagem_label = tk.Label(root, text="Criado com carinho para todos(a) os(a) mains Nunu", justify="center", font=(fonte_bottom))
mensagem_label.pack(side="bottom", pady=10)

root.mainloop()
