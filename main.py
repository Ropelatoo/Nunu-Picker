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

# Janela 800x500
root.geometry("800x500")

# Deixa no meio da tela
largura_janela = 800
altura_janela = 500
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
x_pos = (largura_tela - largura_janela) // 2
y_pos = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

# Starta Var
resultado_var = tk.StringVar()

# Rola dnv
rolar_novamente()

# Fonte
fonte_resultado = ("Helvetica", 14)

# Rotulo resultado
resultado_label = tk.Label(root, textvariable=resultado_var, justify="center", font=fonte_resultado)
resultado_label.pack(pady=10)

# Fonte botão
fonte_botoes = ("Helvetica", 12)

# Cria o botão "Rolar Novamente"
rolar_button = tk.Button(root, text="Rolar Novamente", command=rolar_novamente, font=fonte_botoes, height=2)
rolar_button.pack()

# Cria o botão "Sair"
sair_button = tk.Button(root, text="Sair", command=sair, font=fonte_botoes, height=2)
sair_button.pack()

# Mensagem Discord
espaco_discord_label = tk.Label(root, text="", font=("Helvetica", 10))
espaco_discord_label.pack()

# Fonte
fonte_bottom = ("Helvetica", 10, "italic")

# Msg Discord
discord_label = tk.Label(root, text="Discord: ropelatoo", justify="center", font=(fonte_bottom))
discord_label.pack(side="bottom", pady=10)

# Msg Github
github_label = tk.Label(root, text="Github: Ropelatoo", justify="center", font=(fonte_bottom))
github_label.pack(side="bottom", pady=10)

# Msg Ropelato
criado_por_label = tk.Label(root, text="Criado por Ropelato", justify="center", font=(fonte_bottom))
criado_por_label.pack(side="bottom", pady=10)

# Mensagem
mensagem_label = tk.Label(root, text="Criado com carinho para todos(a) os(a) mains Nunu", justify="center", font=(fonte_bottom))
mensagem_label.pack(side="bottom", pady=10)

root.mainloop()

# Final