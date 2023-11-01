import psycopg2

conn = psycopg2.connect(
    database="postgres", user="postgres", password="alan1234", port="5432"
)
print("Opened database successfully")

comando = conn.cursor()
comando.execute(
    """CREATE TABLE IF NOT EXISTS Agenda (
    id INTEGER PRIMARY KEY NOT NULL, Nome TEXT NOT NULL, Telefone CHAR(11) NOT NULL);"""
)
conn.commit()
print("Table created successfully")
conn.close()
