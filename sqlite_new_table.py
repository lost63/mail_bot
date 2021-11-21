import sqlite3
import path

conn = sqlite3.connect(path.path+"test_db.db")
cursor = conn.cursor()
 
# Создание таблицы
cursor.execute("""CREATE TABLE test_db (ID text, Service text, status text, data_last_modify text, remind_time text, from_email text)""")
