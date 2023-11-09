import tkinter as tk
import sys
import crud as crud


class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppDB()

        # Cria rótulos (labels) e campos de entrada (entry) para código, nome, preço e porcentagem extra.
        self.lbCodigo = tk.Label(win, text="Código do produto")
        self.lbNome = tk.Label(win, text="Nome do produto")
        self.lbPreco = tk.Label(win, text="Preço R$")
        self.lbPorcentagemExtra = tk.Label(win, text="Preço + 10%")

        # Cria um campo de entrada para o código, nome e o preço.
        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry(bd=3)
        self.txtPreco = tk.Entry(bd=3)
        self.txtPorcentagemExtra = tk.Label(win, text="R$0.00", relief="flat")

        # Cria botões para cada ação: cadastrar, atualizar, excluir, limpar, sair, exibir produtos e limpar console.
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
        self.btnLimparConsole = tk.Button(
            win, text="Limpar Console", command=self.limparConsole
        )

        # Cria um campo de texto (Text) para exibir informações e um scrollbar para rolar o texto.
        self.console_text = tk.Text(win, wrap=tk.WORD, height=5, width=50)
        self.scrollbar = tk.Scrollbar(win, command=self.console_text.yview)
        self.console_text.configure(yscrollcommand=self.scrollbar.set)

        # Posiciona os rótulos, campos de entrada, botões e campo de texto na janela.
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
        self.btnLimparConsole.place(x=345, y=300)
        self.console_text.place(x=100, y=350)
        self.scrollbar.place(x=500, y=350, height=90)

        # Redireciona a saída padrão para o campo de texto.
        sys.stdout = TextRedirector(self.console_text, "stdout")

        # Associa um evento de tecla (KeyRelease) ao campo de preço para calcular a porcentagem extra.
        self.txtPreco.bind("<KeyRelease>", self.calcularPorcentagemExtra)

    # Metodo para cadastrar o produto.
    def cadastrarProduto(self):
        try:
            codigo, nome, preco = self.lerCampos()
            preco_com_extra = preco * 1.10
            self.objBD.inserirDados(codigo, nome, preco_com_extra)
            self.txtPorcentagemExtra.config(text=f"{preco_com_extra:.2f}")
            self.limparTela()
        except Exception as e:
            print(f"Erro ao cadastrar o produto: {e}")

    # Metodo para atualizar o produto.
    def atualizarProduto(self):
        try:
            codigo, nome, preco = self.lerCampos()
            preco_com_extra = preco * 1.10
            self.objBD.atualizarDados(codigo, nome, preco_com_extra)
            self.limparTela()
        except Exception as e:
            print(f"Erro ao atualizar o produto: {e}")

    # Metodo para excluir o produto.
    def excluirProduto(self):
        try:
            codigo = int(self.txtCodigo.get())
            if codigo is not None and codigo > 0:
                self.objBD.excluirDados(codigo)
                self.limparTela()
            else:
                print("Nenhum código de produto informado.")
        except ValueError as ve:
            print(f"Erro ao excluir o produto: Código inválido - {ve}")
        except Exception as e:
            print(f"Erro ao excluir o produto: {e}")

    # Metodo para limpar os campos.
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

    # Metodo para ler os campos.
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
            raise ValueError("Erro ao ler os campos: ", e)

    # Metodo para calcular a porcentagem extra.
    def calcularPorcentagemExtra(self, event=None):
        try:
            preco = self.lerPreco()
            porcentagem_extra = preco * 1.1
            self.txtPorcentagemExtra.config(text=f"R${porcentagem_extra:.2f}")
        except ValueError:
            self.txtPorcentagemExtra.config(text="")

    # Metodo para ler o preço.
    def lerPreco(self):
        return float(self.txtPreco.get())

    # Metodo para sair.
    def sair(self):
        janela.destroy()

    # Metodo para exibir os produtos.
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

    # Metodo para limpar a console.
    def limparConsole(self):
        self.console_text.delete("1.0", tk.END)


# Classe para redirecionar a saída padrão para o campo de texto (console).
class TextRedirector:
    def __init__(self, text_widget, tag):
        self.text_widget = (
            text_widget  # O campo de texto onde a saída será redirecionada.
        )
        self.tag = tag  # Um rótulo que pode ser usado para aplicar formatação ao texto inserido.

    def write(self, str):
        self.text_widget.insert(tk.END, str, (self.tag,)) # Insere o texto no console da janela do programa.
        self.text_widget.see(tk.END) # Move para o final do console, sempre exibindo a ultima atualização.


# Cria a janela principal do programa.
janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("PPM - Python Product Manager")
janela.geometry("600x500")
janela.mainloop()
