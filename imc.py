import tkinter
from tkinter import *
from tkinter import ttk
from turtle import width


janela = Tk()
janela.title("Calculadora IMC")
text_orientacao = Label(janela, text="Energy Manager")
janela.geometry("250x250")

infoAltura = Entry(width=10, justify="left")
infoAltura.place(x=15, y=30)

infoPeso = Entry(width=10, justify="left")
infoPeso.place(x=170, y=30)

calcular = Button(width=10, text="Calcular")
calcular.place(x=85, y=125)




janela.mainloop()