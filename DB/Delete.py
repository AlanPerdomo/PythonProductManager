import psycopg2

conn = psycopg2.connect(
    database="postgres", user="postgres", password="alan1234", port="5432"
)
print("Opened database successfully")

comando = conn.cursor()
comando.execute("""DELETE FROM Agenda WHERE id = 1;""")
conn.commit()
cont = comando.rowcount
print("Nome: ", cont)
print("Records deleted successfully")
conn.close()
