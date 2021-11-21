import sqlite3
import path
 
db_name = path.path+"test_db.db"

def insert_data_sql(table, data):
    global db_name
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO "+table+" VALUES ("+data+")")
    conn.commit(); conn.close()

def delete_data_sql(table, Column, data):
    global db_name
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM "+table+" WHERE "+Column+" = '"+data+"'")
    conn.commit(); conn.close()

def update_data_sql(table, data):
    global db_name
    global db_table_name
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE "+table+" SET "+data)
    conn.commit(); conn.close()

def sql_get_posts():
    global db_name
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    with conn:
        cursor.execute("SELECT * FROM "+db_table_name)
        print(cursor.fetchall())

def sql_row_names(table):
        global db_name
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM "+table)
        names = [description[0] for description in cursor.description]
        names = cursor.fetchall()
        return names

def sql_select_data(db_table_name, column_, name_):
        global db_name
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM "+db_table_name)
        names = [description[0] for description in cursor.description]
        cursor.execute("SELECT * FROM "+db_table_name+" WHERE "+column_+"='"+name_+"';")
        rows = cursor.fetchall()
        for row in rows:
            names.append(row)
        conn.commit(); conn.close()
        return names