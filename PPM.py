import tkinter as tk
from crud import AppDB

class PrincipalBD:
    def __init__(self, win):
        self.objBD = AppDB()  
        self.lbCodigo = tk.Label(win, text="Código do produto")
        self.lblNome = tk.Label(win, text="Nome do produto")
        self.lblPreco = tk.Label(win, text="Preço")

        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()

        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar = tk.Button(win, text='Atualizar')
        self.btnExcluir = tk.Button(win, text='Excluir')
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela)

    def fCadastrarProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos()
            self.objBD.inserir(codigo, nome, preco)
            self.fLimparTela()
            print("Produto cadastrado com sucesso!")
        except:
            print("Erro ao cadastrar o produto")

    def fLimparTela(self):
        # Adicione a lógica para limpar a tela aqui
        pass

janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("PPM - Python Product Manager")
janela.geometry("300x500")
janela.mainloop()