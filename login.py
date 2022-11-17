from tkinter import *


tela = Tk()
tela.title("Login")
tela.geometry("230x200")

usuarioLabel = Label(text="Nome de usuário:")
usuarioLabel.place(x=60, y=10)
usuarioEntry = Entry(width=10, justify="left")
usuarioEntry.place(x=70, y=35)

senhaLabel = Label(text="Senha:")
senhaLabel.place(x=60, y=50)
senhaEntry = Entry(width=10, justify="left")
senhaEntry.place(x=70, y=75)

btLogar = Button(width=10, text="Logar")
btLogar.place(x=60, y=100)

infoLabel = Label(text="Caso esquecer cadastro, consultar ADM")
infoLabel.place(x=5,y=170)

tela.mainloop()