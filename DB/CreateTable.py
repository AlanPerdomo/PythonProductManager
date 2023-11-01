import psycopg2

conn = psycopg2.connect(
    database="postgres", user="postgres", password="alan1234", port="5432"
)
print("Opened database successfully")

comando = conn.cursor()
comando.execute(
    """CREATE TABLE IF NOT EXISTS produto(
    id SERIAL PRIMARY KEY NOT NULL, Nome TEXT NOT NULL, Codigo INTEGER NOT NULL, Preco float NOT NULL);"""
)
conn.commit()
print("Table created successfully")
conn.close()
