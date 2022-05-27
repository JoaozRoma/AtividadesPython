import sqlite3
arq = "database.db"
conn = sqlite3.connect(arq)
cursor = conn.cursor()

sql = """CREATE TABLE professor (
          id integer PRIMARY KEY AUTOINCREMENT,
          nome text,
          disciplina text,
          turma text
        );"""
cursor.execute(sql)

conn.close()
