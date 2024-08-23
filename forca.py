import tkinter as tk
from tkinter import Label, Entry
import random
import string

class JogoAdivinhacao(tk.Frame):
    def __init__(self, mestre=None):
        super().__init__(mestre)
        self.mestre = mestre
        self.pack()
        self.criar_widgets()
        self.gerar_palavras_aleatorias()
        self.carregar_palavra()

    def criar_widgets(self):
        self.rotulo_palavra = Label(self)
        self.rotulo_palavra["text"] = "Adivinhe a palavra"
        self.rotulo_palavra.pack(side="top")
        self.rotulo_palavra_adivinhada = Label(self)
        self.rotulo_palavra_adivinhada.pack(side="top")
        self.entrada = Entry(self)
        self.entrada.bind('<Return>', self.verificar_palpite)
        self.entrada.pack(side="bottom")

    def gerar_palavras_aleatorias(self):
        palavras_aleatorias = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8))) for _ in range(10)]
        with open("palavra.txt", "w") as arquivo:
            for palavra in palavras_aleatorias:
                arquivo.write(palavra + "\n")

    def carregar_palavra(self):
        with open("palavra.txt", "r") as arquivo:
            self.palavras = [palavra.strip().lower() for palavra in arquivo.readlines()]
            self.palavra = random.choice(self.palavras)
            self.palavra_adivinhada = ["-"] * len(self.palavra)
            self.atualizar_rotulo_palavra_adivinhada()

    def atualizar_rotulo_palavra_adivinhada(self):
        self.rotulo_palavra_adivinhada["text"] = " ".join(self.palavra_adivinhada)

    def verificar_palpite(self, event):
        palpite = self.entrada.get().lower()
        self.entrada.delete(0, tk.END)
        if len(palpite) == 1 and palpite.isalpha():
            for i, letra in enumerate(self.palavra):
                if letra == palpite:
                    self.palavra_adivinhada[i] = palpite
            self.atualizar_rotulo_palavra_adivinhada()
            if "-" not in self.palavra_adivinhada:
                self.rotulo_palavra["text"] = "Você adivinhou a palavra!"

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoAdivinhacao(mestre=root)
    app.mainloop()
