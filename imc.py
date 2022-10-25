from cProfile import label
import tkinter
from tkinter import *
from tkinter import ttk
from turtle import width
import tkinter as tk



janela = Tk()
janela.title("Calculadora IMC")

janela.geometry("250x250")

#------FUNÇÕES--------#




def bt_onclick():
    entAltura = float(infoAltura.get())
    entPeso = float(infoPeso.get())
    
    imc =  float(entPeso /(entAltura ** 2))
    
    resultado1["text"] = imc





#--------------------------------------------------#
labelAltura = Label(text="Informe sua altura:")
labelAltura.place(x=5, y=5)

infoAltura = Entry(width=10, justify="left")
infoAltura.place(x=15, y=30)
#--------------------------------------------------#


labelPeso = Label(text="Informe seu peso:")
labelPeso.place(x=145, y=5)

infoPeso = Entry(width=10, justify="left")
infoPeso.place(x=170, y=30)
#---------------------------------------------------#


btCalcular = Button(width=10, text="Calcular", command = bt_onclick)
btCalcular.place(x=85, y=125)


#---------------------------------------------------#
resultado1 = Label(janela, text=("Resultado aqui"))
resultado1.place(x=32, y=170)



janela.mainloop()