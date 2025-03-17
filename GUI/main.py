import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk


cout = 0
def on_click():
    global cout 
    cout += 1
    messagebox.showinfo(f"Olá!", f"Você clicou no botão {cout} Vezes")

def cadastro():
    return True
    
janela = tk.Tk()
janela.title("APP DE TESTE")
janela.geometry("1280x720")

rotulo = tk.Label(janela, text="Olá, Mundo", font=("Arial", 14))
rotulo.pack(pady=10)

botao = tk.Button(janela, text="Botao", command=on_click)
botao.pack(pady=5)
btn = tk.Button(janela, text="Login")
btn.pack(pady=1)

texto = tk.Label(janela, text="Insira seu nome", font=("Arial", 14))
texto.pack(pady=10)

framo = tk.Frame(janela)
framo.pack()
entry = tk.Entry(framo)
entry.pack(pady= 2)

janela.mainloop()
