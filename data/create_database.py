import sqlite3
import os

def create_database():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(dir_path, 'inventory.db')
    sql_file_path = os.path.join(dir_path, 'db_init.sql')
    conn = sqlite3.connect(db_path)
    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print("Database has been created and the SQL script executed.")
if __name__ == '__main__':
    create_database()
