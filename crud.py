import psycopg2

class AppDB:
    def __init__(self):
        print("Método Construtor")

    def abrirConexao(self):
        try:
            self.connetion = psycopg2.connect(
                user="postgres",
                password="alan1234",
                host="127.0.0.1",
                database="postgres",
            )
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao conectar ao banco de dados", error)