import tkinter as tk
import crud as crud


class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppDB()
        self.lbCodigo = tk.Label(win, text="Código do produto")
        self.lbNome = tk.Label(win, text="Nome do produto")
        self.lbPreco = tk.Label(win, text="Preço R$")
        self.lbPorcentagemExtra = tk.Label(win, text="Preço + 10%")

        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry(bd=3)
        self.txtPreco = tk.Entry(bd=3)
        self.txtPorcentagemExtra = tk.Label(win, text="R$0.00", relief="flat")

        self.btnCadastrar = tk.Button(
            win, text="Cadastrar", command=self.cadastrarProduto
        )
        self.btnAtualizar = tk.Button(
            win, text="Atualizar", command=self.atualizarProduto
        )
        self.btnExcluir = tk.Button(win, text="Excluir", command=self.excluirProduto)
        self.btnLimpar = tk.Button(win, text="Limpar", command=self.limparTela)
        self.btnSair = tk.Button(win, text="Sair", command=self.sair)
        self.btnExibirProdutos = tk.Button(
            win, text="Exibir Produtos", command=self.exibirProdutos
        )

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
        self.btnSair.place(x=100, y=300)
        self.btnExibirProdutos.place(x=200, y=300)

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
            preco_com_extra = preco * 1.10
            self.objBD.atualizarDados(codigo, nome, preco_com_extra)
            self.limparTela()
            print("Produto atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar o produto: {e}")

    def excluirProduto(self):
        try:
            codigo = int(self.txtCodigo.get())
            if codigo is not None and codigo > 0:
                self.objBD.excluirDados(codigo)
                self.limparTela()
                print(f"Produto com código {codigo} excluído com sucesso!")
            else:
                print("Nenhum código de produto informado.")
        except ValueError as ve:
            print(f"Erro ao excluir o produto: Código inválido - {ve}")
        except Exception as e:
            print(f"Erro ao excluir o produto: {e}")

    def limparTela(self):
        try:
            if (
                self.txtCodigo.get() == ""
                and self.txtNome.get() == ""
                and self.txtPreco.get() == ""
            ):
                print("Campos ja estão limpos")
            else:
                self.txtCodigo.delete(0, tk.END)
                self.txtNome.delete(0, tk.END)
                self.txtPreco.delete(0, tk.END)
                self.txtPorcentagemExtra.config(text="R$0.00")
                print("Campos limpos com sucesso")
        except Exception as e:
            print(f"Erro ao limpar os campos: {e}")

    def lerCampos(self):
        try:
            codigo = int(self.txtCodigo.get())
            if codigo is None or codigo < 0:
                raise ValueError("Código inválido")
            nome = self.txtNome.get()
            preco = float(self.txtPreco.get())
            if preco is None or preco < 0:
                raise ValueError("Preço inválido")
            print("Campos lidos com sucesso")
            return (codigo, nome, preco)
        except ValueError as e:
            self.txtCodigo.config(fg="red")
            self.txtPreco.config(fg="red")
            self.txtCodigo.insert(tk.END, "Código inválido")
            self.txtPreco.insert(tk.END, "Preço inválido")
            print(f"Erro ao ler os campos: ", e)
            raise ValueError("Erro ao ler os campos: ", e)

    def calcularPorcentagemExtra(self, event=None):
        try:
            preco = self.lerPreco()
            porcentagem_extra = preco * 1.1
            self.txtPorcentagemExtra.config(text=f"R${porcentagem_extra:.2f}")
        except ValueError:
            self.txtPorcentagemExtra.config(text="")

    def lerPreco(self):
        return float(self.txtPreco.get())

    def sair(self):
        janela.destroy()

    def exibirProdutos(self):
        try:
            produtos = self.objBD.getProdutos()
            for produto in produtos:
                print(
                    f"Código: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]:.2f}"
                )

            lista_produtos = tk.Toplevel()
            lista_produtos.title("Lista de Produtos cadastrados")
            lista_text = tk.Text(lista_produtos, wrap=tk.WORD)
            lista_text.pack()

            for produto in produtos:
                lista_text.insert(
                    tk.END,
                    f"Código: {produto[2]}\t\t\tNome: {produto[1]}\t\t\tPreco: R${produto[3]:.2f}\n",
                )

        except Exception as e:
            print(f"Erro ao exibir os produtos: {e}")


janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("PPM - Python Product Manager")
janela.geometry("600x350")
janela.mainloop()
