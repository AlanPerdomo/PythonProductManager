import psycopg2

conn = psycopg2.connect(
    database="postgres", user="postgres", password="alan1234", port="5432"
)
print("Opened database successfully")
comando = conn.cursor()
comando.execute("""SELECT * FROM AGENDA where id = 2 ;""")
registro = comando.fetchall()
print("Nome: ", registro)
conn.commit()

print("Records selected successfully")
conn.close()
