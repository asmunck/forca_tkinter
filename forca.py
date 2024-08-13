import tkinter as tk
from tkinter import Frame, Label, Entry
import random

class Forca(Frame):
    def __init__(self, mestre=None):
        super().__init__(mestre)
        self.mestre = mestre
        self.pack()
        self.criar_widgets()

    def criar_widgets(self):
        self.rotulo_palavra = Label(self)
        self.rotulo_palavra["text"] = "Adivinhe a palavra"
        self.rotulo_palavra.pack(side="top")
        self.rotulo_palavra_adivinhada = Label(self)
        self.rotulo_palavra_adivinhada.pack(side="top")
        self.entrada = Entry(self)
        self.entrada.bind('<Return>', self.verificar_palpite)
        self.entrada.pack(side="bottom")

    def carregar_palavra(self):
        with open("palavra.txt", "r") as arquivo:
            self.palavras = [palavra.strip().lower() for palavra in arquivo.readlines()]
            self.palavra = random.choice(self.palavras)
            self.palavra_adivinhada = ["-"] * len(self.palavra)
            self.atualizar_rotulo_palavra_adivinhada()

    def atualizar_rotulo_palavra_adivinhada(self):
        self.rotulo_palavra_adivinhada["text"] = "".join(self.palavra_adivinhada)

    def verificar_palpite(self, evento):
        palpite = self.entrada.get().lower()
        self.entrada.delete(0, 'end')
        for i, letra in enumerate(self.palavra):
            if letra == palpite:
                self.palavra_adivinhada[i] = palpite
        self.atualizar_rotulo_palavra_adivinhada()

raiz = tk.Tk()
app = Forca(mestre=raiz)
app.carregar_palavra()
app.mainloop()
