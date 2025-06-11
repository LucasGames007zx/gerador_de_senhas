import tkinter as tk
import random
import string
from tkinter import messagebox

# Função para gerar senha
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Função para lidar com o clique no botão
def ao_gerar_senha():
    dificuldade = dificuldade_var.get()
    if dificuldade == "facil":
        tamanho = 8
    elif dificuldade == "media":
        tamanho = 12
    elif dificuldade == "dificil":
        tamanho = 16
    else:
        messagebox.showwarning("Aviso", "Selecione uma dificuldade.")
        return

    senha = gerar_senha(tamanho)
    senha_var.set(senha)

# Função para copiar senha
def copiar_senha():
    senha = senha_var.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência.")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha gerada para copiar.")

# Interface Tkinter
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("400x250")
root.resizable(False, False)

# Variáveis
dificuldade_var = tk.StringVar()
senha_var = tk.StringVar()

# Layout
tk.Label(root, text="Escolha a dificuldade:", font=("Arial", 12)).pack(pady=10)

tk.Radiobutton(root, text="Fácil (8)", variable=dificuldade_var, value="facil").pack()
tk.Radiobutton(root, text="Média (12)", variable=dificuldade_var, value="media").pack()
tk.Radiobutton(root, text="Difícil (16)", variable=dificuldade_var, value="dificil").pack()

tk.Button(root, text="Gerar Senha", command=ao_gerar_senha, bg="#4CAF50", fg="white").pack(pady=10)

tk.Entry(root, textvariable=senha_var, font=("Arial", 14), justify="center").pack(pady=5)

tk.Button(root, text="Copiar Senha", command=copiar_senha).pack(pady=5)

# Iniciar a interface
root.mainloop()


#comentário do ale
