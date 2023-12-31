import psycopg2


class AppDB:
    def __init__(self):
        print("Conectando ao banco de dados")

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="alan1234",
                host="127.0.0.1",
                database="postgres",
            )
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao conectar ao banco de dados", error)

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM public.produto WHERE codigo = %s", (codigo,))
            existing_product = cursor.fetchone()  # Verifica se o registro existe.
            if existing_product:
                print(
                    "Produto ja existe"
                )  # Se o registro existir, Informa que o registro ja existe.
                return
            else:
                postgres_insert_query = """ INSERT INTO public."produto"("codigo","nome","preco") VALUES (%s,%s,%s)"""
                record_to_insert = (codigo, nome, preco)
                cursor.execute(
                    postgres_insert_query, record_to_insert
                )  # Executa a query para inserir os dados com os metodos codigo, nome e preco passados.
                self.connection.commit()
                count = cursor.rowcount
                print(
                    count, "Registro inserido com sucesso"
                )  # Informa quantos registros foram inseridos com sucesso.
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao inserir dados", error)  # Informa o erro.
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão fechada")  # Encerra a conexão.

    # Metodo para atualizar dados
    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_update_query = """Update public."produto" set "nome" = %s,
            "preco" = %s where "codigo" = %s"""
            cursor.execute(
                sql_update_query, (nome, preco, codigo)
            )  # Executa a query para atualizar os dados com os parametros nome, preco e codigo passados.
            self.connection.commit()  # Confirma a atualização.
            count = cursor.rowcount
            print(
                count, "Registro atualizado com sucesso! "
            )  # Informa quantos registros foram atualizados.
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from public."produto"
            where "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)  # Imprime o registro após a atualização.
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao atualizar dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão fechada")

    # Metodo para excluir dados
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = """Delete from public."produto" where "codigo" = %s"""
            cursor.execute(sql_delete_query, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(
                count, "Registro excluído com sucesso"
            )  # Informa quantos registros foram excluídos
            print(
                f"Produto com código {codigo} excluído com sucesso!"
            )  # Informa o codigo do produto que foi excluído
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao excluir dados", error)
                # No caso de falha, informa o erro.
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão fechada")
                # Fecha a conexão com o banco de dados apos a consulta.

    # Metodo para buscar os produtos no banco de dados
    def getProdutos(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM public.produto")
            produtos = cursor.fetchall()
            return produtos
            # Busca todos os produtos na tabela 'produto' e retorna como uma lista de registros.
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao buscar dados", error)
                # No caso de falha, informa o erro.
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão fechada")
                # Fecha a conexão com o banco de dados apos a consulta.
