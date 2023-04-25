import mysql.connector
from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox


class JanelaImc:

    def __init__(self):
        '''
        metodo que cria a janela tkinter, recebe o nome, altura, peso, sexo, idade.
        '''
        self.janela = Tk()
        self.janela.title("Calculadora IMC")
        self.janela.geometry("300x240")

        self._infoNome = Entry(width=10, justify="left")
        self._infoNome.place(x=50, y=5)
        self.labelNome = Label(text="Nome:")
        self.labelNome.place(x=5, y=5)

        @property
        def infoNome(self):
            return self._nome

        @infoNome.setter
        def infoNome(self, novo_nome):
            self._nome = novo_nome.upper()

        self.infoAltura = Entry(width=10, justify="left")
        self.infoAltura.place(x=135, y=30)
        self.labelAltura = Label(text="Altura em Centímetro:")
        self.labelAltura.place(x=5, y=30)

        self.infoPeso = Entry(width=10, justify="left")
        self.infoPeso.place(x=115, y=60)
        self.labelPeso = Label(text="Informe seu peso:")
        self.labelPeso.place(x=5, y=60)

        self.labelSexo = Label(text="Informe seu sexo:")
        self.labelSexo.place(x=5, y=90)
        self.listSexo = ["Masculino", "Feminino"]
        self.cb_Sexo = ttk.Combobox(width=10, values=self.listSexo)
        self.cb_Sexo.set("")
        self.cb_Sexo.pack()
        self.cb_Sexo.place(x=110, y=90)

        self.infoIdade = Entry(width=10, justify="left")
        self.infoIdade.place(x=115, y=120)
        self.labelIdade = Label(text="Informe sua idade:")
        self.labelIdade.place(x=5, y=120)

        self.btCalcular = Button(width=10, text="Calcular", command=self.bt_oneclick)
        self.btCalcular.place(x=90, y=160)

        self.resultado1 = Label(self.janela, text=("Resultado aqui:"))
        self.resultado1.place(x=3, y=190)
        self.resultado2 = Label(self.janela, text=("Taxa de metabolismo basal:"))
        self.resultado2.place(x=3, y=210)

        self.data_hora = Label(self.janela, text=(""))
        self.data_hora.place(x=190, y=4)


        self.btVisualizar = Button(width=10, text="Visualizar", command=self.visualizar)
        self.btVisualizar.place(x=200, y=160)

    def bt_oneclick(self):
        '''
        Metodo usado para fazer todo o calculo do imc e tmb, a partir do botão calcular,
        o metodo pega a altura, peso, idade, nome e sexo, retornando a imc, o tmb, a situacao que
        o individuo se encontra e a data de hoje com a hora.
        :return:
        '''
        try:
            altura = float(self.infoAltura.get())
            peso = float(self.infoPeso.get())
            idade = int(self.infoIdade.get())
            nome = str(self._infoNome.get())
            sexo = self.cb_Sexo.get()

            imc = peso / ((altura / 100) ** 2)
            tmb = 0

            if sexo == "Masculino":
                tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
            elif sexo == "Feminino":
                tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

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


            self.resultado1.config(text=f"O IMC é {imc:.2f} e a situação está {situacao}")

            self.resultado2.config(text=f"A sua taxa de metabolismo basal é: {tmb:.2f} calorias")
            dataAtual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.data_hora.config(text=f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


            conexao = JanelaImc.__criar_conexao()
            cursor = conexao.cursor()

            comando = f'INSERT INTO cliente (nome, altura, peso, sexo, idade, imc, situacao, tmb, data) VALUES ("{nome}", {altura}, {peso}, "{sexo}", {idade}, {imc:.2f},"{situacao}", "{tmb:.2f}", "{dataAtual}");'
            cursor.execute(comando)
            conexao.commit()  # edita o banco de dados

            cursor.close()
            conexao.close()

        except ValueError as erro:
            messagebox.showerror("Erro", "Revise suas informações e corrija.")

    @staticmethod
    def visualizar():
        '''
        Metodo usado para mostrar todos os cadastrados no banco de dados.
        :return:
        '''
        conexao = JanelaImc.__criar_conexao()
        cursor = conexao.cursor()

        comando = f'SELECT * FROM cliente;'
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        registros = ""
        for id_cliente, nome, altura, peso, sexo, idade, imc, situacao, tmb, data in resultado:
            print(f"Id: {id_cliente}, Nome: {nome}, altura: {altura}, Peso: {peso}, Sexo: {sexo}, Idade: {idade}, Imc: {imc:.2f}, Situação: {situacao}, Tmb: {tmb}, Data: {data}\n")
            registro = f"Id: {id_cliente}, Nome: {nome}, altura: {altura}, Peso: {peso}, Sexo: {sexo}, Idade: {idade}, Imc: {imc:.2f}, Situação: {situacao}, Tmb: {tmb}, Data: {data}\n"
            registros += registro
        view = Tk()
        view.title("Meus Clientes")

        label = Label(view, text=(f"{registros}" ))
        label.pack()
        view.mainloop()

        cursor.close()
        conexao.close()

    def executar(self):
        self.janela.mainloop()

    @staticmethod
    def __criar_conexao():
        '''
        Metodo usado para criar conexão com o banco de dados
        :return:
        '''
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='imc'
        )
        return conexao