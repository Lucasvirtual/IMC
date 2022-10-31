from cProfile import label
from pickletools import int4
import tkinter
from tkinter import *
from tkinter import ttk
from turtle import bgcolor, width
import tkinter as tk


janela = Tk()
janela.title("Calculadora IMC")
janela.geometry("350x250")


#--------FUNÇÕES--------#

def bt_onclick():
    entAltura = float(infoAltura.get())
    entPeso = float(infoPeso.get())
    entIdade = int(infoIdade.get())
    entSexo = str(cb_Sexo.get())
    alturaM = entAltura / 100
    imc  =  float(entPeso /(alturaM ** 2))
    
 
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
    
    resultado1["text"] = ("O IMC é {:.2f} e a situação está {}").format(imc,situacao)
    
#----------------------------------------------------------------------------------------# 
    
    if cb_Sexo.get() == "Masculino":
        tmb = float(66 + (13.7 * entPeso) + (5.0 * entAltura) - (6.8 * entIdade))


    elif cb_Sexo.get() == "Feminino":
        tmb = float(665 + (9.6 * entPeso) + (1.8 * entAltura) - (4.7 * entIdade)) 

    else:
        tmb = ("Invalido")
 
   
    resultado2["text"] = ("A sua taxa de metabolismo basal é: {:.2f} calorias").format(tmb)


#--------------------------------------------------------#
labelAltura = Label(text="Informe sua altura em Centímetros:")
labelAltura.place(x=5, y=5)

infoAltura = Entry(width=10, justify="left")
infoAltura.place(x=15, y=25)
#--------------------------------------------------------#


labelPeso = Label(text="Informe seu peso:")
labelPeso.place(x=5, y=45)

infoPeso = Entry(width=10, justify="left")
infoPeso.place(x=15, y=70)
#--------------------------------------------------------#

labelSexo = Label(text="Informe seu sexo:")
labelSexo.place(x=5, y=85)

listSexo=["Masculino","Feminino"]

cb_Sexo=ttk.Combobox(width=10,values=listSexo)
cb_Sexo.set("")
cb_Sexo.pack()
cb_Sexo.place(x=15, y=105)


#--------------------------------------------------------#
labelIdade = Label(text="Informe sua idade:")
labelIdade.place(x=5, y=130)

infoIdade = Entry(width=10, justify="left")
infoIdade.place(x=15, y=150)
#--------------------------------------------------------#


btCalcular = Button(width=10, text="Calcular", command = bt_onclick)
btCalcular.place(x=85, y=170)


#--------------------------------------------------------#
resultado1 = Label(janela, text=("Resultado aqui:"))
resultado1.place(x=3, y=200)

resultado2 = Label(janela, text=("Taxa de metabolismo basal:"))
resultado2.place(x=3, y=220)




janela.mainloop()