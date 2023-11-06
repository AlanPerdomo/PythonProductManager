import tkinter as tk
from crud import AppDB


class PrincipalBD:
    def __init__(self, win):
        self.objBD = AppDB()
        self.lbCodigo = tk.Label(win, text="Código do produto")
        self.lbNome = tk.Label(win, text="Nome do produto")
        self.lbPreco = tk.Label(win, text="Preço")
        self.lbPorcentagemExtra = tk.Label(win, text="Porcentagem extra")

        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()
        self.txtPorcentagemExtra = tk.Label(win, text="", relief="solid")

        self.btnCadastrar = tk.Button(
            win, text="Cadastrar", command=self.cadastrarProduto
        )
        self.btnAtualizar = tk.Button(
            win, text="Atualizar", command=self.atualizarProduto
        )
        self.btnExcluir = tk.Button(win, text="Excluir", command=self.excluirProduto)
        self.btnLimpar = tk.Button(win, text="Limpar", command=self.limparTela)

        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lbNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lbPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)

        self.lbPorcentagemExtra.place(x=100, y=200)
        self.txtPorcentagemExtra.place(x=250, y=200)

        self.btnCadastrar.place(x=100, y=250)
        self.btnAtualizar.place(x=200, y=250)
        self.btnExcluir.place(x=300, y=250)
        self.btnLimpar.place(x=400, y=250)

        self.txtPreco.bind("<KeyRelease>", self.calcularPorcentagemExtra)

    def cadastrarProduto(self):
        try:
            codigo, nome, preco = self.lerCampos()
            preco_com_extra = preco * 1.10
            self.objBD.inserirDados(codigo, nome, preco_com_extra)
            self.txtPorcentagemExtra.config(text=f"{preco_com_extra:.2f}")
            self.limparTela()
            print("Produto cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar o produto: {e}")

    def atualizarProduto(self):
        try:
            codigo, nome, preco = self.lerCampos()
            self.objBD.atualizarDados(codigo, nome, preco)
            self.limparTela()
            print("Produto atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar o produto: {e}")

    def excluirProduto(self):
        try:
            codigo, nome, preco = self.lerCampos()
            self.objBD.excluirDados(codigo)
            self.limparTela()
            print("Produto excluído com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir o produto: {e}")

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

    def calcularPorcentagemExtra(self, event=None):
        try:
            preco = self.lerPreco()
            porcentagem_extra = preco * 0.1
            self.txtPorcentagemExtra.config(text=f"{porcentagem_extra:.2f}")
        except ValueError:
            self.txtPorcentagemExtra.config(text="")

    def lerPreco(self):
        return float(self.txtPreco.get())


janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("PPM - Python Product Manager")
janela.geometry("600x350")
janela.mainloop()
