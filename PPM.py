import tkinter as tk
from crud import AppDB


class PrincipalBD:
    def __init__(self, win):
        self.objBD = AppDB()
        self.lbCodigo = tk.Label(win, text="Código do produto")
        self.lbNome = tk.Label(win, text="Nome do produto")
        self.lbPreco = tk.Label(win, text="Preço")

        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()

        self.btnCadastrar = tk.Button(
            win, text="Cadastrar", command=self.cadastrarProduto
        )
        self.btnAtualizar = tk.Button(win, text="Atualizar")
        self.btnExcluir = tk.Button(win, text="Excluir")
        self.btnLimpar = tk.Button(win, text="Limpar", command=self.limparTela)

        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lbNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lbPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

    def cadastrarProduto(self):
        try:
            codigo, nome, preco = self.lerCampos()
            self.objBD.inserirDados(codigo, nome, preco)
            self.limparTela()
            print("Produto cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar o produto: {e}")

    def limparTela(self):
        try:
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print("Campos limpos com sucesso")
        except Exception as e:
            print(f"Erro ao limpar os campos: {e}")

    def lerCampos(self):
        try:
            codigo = int(self.txtCodigo.get())
            nome = self.txtNome.get()
            preco = float(self.txtPreco.get())
            print("Leitura de dados com sucesso")
            return (codigo, nome, preco)
        except ValueError as e:
            raise ValueError("Erro ao ler os campos: ", e)


janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("PPM - Python Product Manager")
janela.geometry("600x350")
janela.mainloop()
