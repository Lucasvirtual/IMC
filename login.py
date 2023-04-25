from tkinter import *
from tkinter import messagebox
from imc import JanelaImc

class Login:

    def __init__(self, root):
        self.root = root
        self.root.title("Tela de Login")
        self.root.geometry("230x110")
        self.root.resizable(False, False)

        self.username = StringVar()
        self.password = StringVar()


        Label(self.root, text="Nome de Usuário:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
        Label(self.root, text="Senha:").grid(row=1, column=0, padx=5, pady=5, sticky=W)

        Entry(self.root, textvariable=self.username, width=15).grid(row=0, column=1, padx=5, pady=5, sticky=W)
        Entry(self.root, textvariable=self.password, show="*", width=15).grid(row=1, column=1, padx=5, pady=5, sticky=W)

        Button(self.root, text="Entrar", command=self.login).grid(row=2, column=1, padx=5, pady=5, sticky=E)

    def login(self):
        if self.username.get() == "admin" and self.password.get() == "admin":
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.root.destroy()
            JanelaImc()

        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")
            self.username.set("")
            self.password.set("")


root = Tk()
login = Login(root)
root.mainloop()