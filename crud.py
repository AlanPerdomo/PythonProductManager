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
            existing_product = cursor.fetchone()
            if existing_product:
                print("Produto ja existe")
                return
            else:
                postgres_insert_query = """ INSERT INTO public."produto"("codigo","nome","preco") VALUES (%s,%s,%s)"""
                record_to_insert = (codigo, nome, preco)
                cursor.execute(postgres_insert_query, record_to_insert)
                self.connection.commit()
                count = cursor.rowcount
                print(count, "Registro inserido com sucesso")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao inserir dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão fechada")

    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_update_query = """Update public."produto" set "nome" = %s,
            "preco" = %s where "codigo" = %s"""
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso! ")
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from public."produto"
            where "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao atualizar dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão fechada")

    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = """Delete from public."produto" where "codigo" = %s"""
            cursor.execute(sql_delete_query, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao excluir dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão fechada")

    def getProdutos(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM public.produto")
            produtos = cursor.fetchall()
            return produtos
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao buscar dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão fechada")
