import psycopg2


class AppDB:
    def __init__(self):
        print("Método Construtor")

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
