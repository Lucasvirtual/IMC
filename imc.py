from cProfile import label
import tkinter
from tkinter import *
from tkinter import ttk
from turtle import width
import tkinter as tk


janela = Tk()
janela.title("Calculadora IMC")

janela.geometry("250x250")

#--------FUNÇÕES--------#

def bt_onclick():
    entAltura = float(infoAltura.get())
    entPeso = float(infoPeso.get())
    entIdade = int(infoIdade.get())
    imc  =  float(entPeso /(entAltura ** 2))
    
    if imc <= 18.5: 
        situacao = "Magreza"

    elif imc >= 18.5 and imc <= 24.9:
        situacao = "Normal"

    elif imc >= 25 and imc <= 29.9:
        situacao = "Sobrepeso 1"

    elif imc >= 30 and imc <= 39.9:
        situacao = "Obesidade 2" 

    else:
        situacao = "Obesidade Grave 3"
    
    if infoSexo == "m" and "M":
        tmb = 66 + (13.7 * entPeso) + (5.0 * entAltura) - (6.8 * entIdade)
    
    
    
    resultado1["text"] = ("O IMC é {:.2f} e a situação {}").format(imc,situacao)
    resultado2["text"] = tmb


#--------------------------------------------------------#
labelAltura = Label(text="Informe sua altura:")
labelAltura.place(x=5, y=5)

infoAltura = Entry(width=10, justify="left")
infoAltura.place(x=15, y=30)
#--------------------------------------------------------#


labelPeso = Label(text="Informe seu peso:")
labelPeso.place(x=5, y=50)

infoPeso = Entry(width=10, justify="left")
infoPeso.place(x=15, y=75)
#--------------------------------------------------------#


labelSexo = Label(text="Informe seu sexo:")
labelSexo.place(x=5, y=90)

infoSexo = Entry(width=10, justify="left")
infoSexo.place(x=15, y=115)


#--------------------------------------------------------#
labelIdade = Label(text="Informe sua idade:")
labelIdade.place(x=5, y=135)

infoIdade = Entry(width=10, justify="left")
infoIdade.place(x=15, y=155)
#--------------------------------------------------------#


btCalcular = Button(width=10, text="Calcular", command = bt_onclick)
btCalcular.place(x=85, y=170)


#--------------------------------------------------------#
resultado1 = Label(janela, text=("Resultado aqui:"))
resultado1.place(x=3, y=200)

resultado2 = Label(janela, text=("Taxa de metabolismo basal:"))
resultado2.place(x=3, y=220)




janela.mainloop()