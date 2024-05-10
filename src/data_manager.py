import sqlite3

class DataManager   :
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        

    def get_connection(self):
        return self.connection
    
    def add_item(self, ingredient_id, type, name, quantity, expiration_date, in_date):
        self.cursor.execute('INSERT INTO ingredient VALUES (?, ?, ?, ?, ?, ?)', (ingredient_id, type, name, quantity, expiration_date, in_date))
        self.connection.commit()

    def delete_item(self, ingredient_id, id):
        self.cursor.execute('DELETE FROM ingredient WHERE ingredient_id = ? AND id = ?', (ingredient_id, id))
        self.connection.commit()
