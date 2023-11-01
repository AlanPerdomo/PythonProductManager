import psycopg2

conn = psycopg2.connect(
    database="postgres", user="postgres", password="alan1234", port="5432"
)
print("Opened database successfully")

comando = conn.cursor()
comando.execute(
    """INSERT INTO Agenda (id, Nome, Telefone) VALUES (1, 'Alan', '21976140325');"""
)
conn.commit()
print("Records created successfully")
conn.close()
