import tkinter as tk
from tkinter import messagebox

def on_click():
    messagebox.showinfo("Olá!", "Você clicou no botão!")

janela = tk.Tk()
janela.title("Minha Interface Gráfica")
janela.geometry("300x200")

rotulo = tk.Label(janela, text="Olá, Mundo", font=("Arial", 14))
rotulo.pack(pady=10)

botao = tk.Button(janela, text="Clique aqui", command=on_click)
botao.pack(pady=5)

janela.mainloop()
