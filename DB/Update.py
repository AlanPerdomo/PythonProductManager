import psycopg2

conn = psycopg2.connect(
    database="postgres", user="postgres", password="alan1234", port="5432"
)
print("Opened database successfully")
comando = conn.cursor()
comando.execute("""SELECT * FROM AGENDA where id = 1 ;""")
registros = comando.fetchone()
print("Nome: ", registros)
comando.execute("""UPDATE AGENDA SET telefone = '21975701099' WHERE id = 1;""")
conn.commit()
print("Records updated successfully")
comando = conn.cursor()
print("Consultando novamente:")
comando.execute("""SELECT * FROM AGENDA where id = 1 ;""")
registro = comando.fetchone()
print("Nome: ", registro)
conn.commit()
conn.close()
