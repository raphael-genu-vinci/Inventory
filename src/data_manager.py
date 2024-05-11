import sqlite3
import os 
from info import ingredients_requirements

class DataManager:
    def __init__(self, db_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        db_path = os.path.join(dir_path, db_name)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        

    def get_connection(self):
        return self.connection
    
    def add_item(self, ingredient_id, type, name, quantity, expiration_date, in_date):
        self.cursor.execute('INSERT INTO ingredient VALUES (?, ?, ?, ?, ?, ?)', (ingredient_id, type, name, quantity, expiration_date, in_date))
        self.connection.commit()

    def delete_item(self, ingredient_id, id):
        self.cursor.execute('DELETE FROM ingredient WHERE ingredient_id = ? AND id = ?', (ingredient_id, id))
        self.connection.commit()

    def get_all_items(self):
        quantity_by_name = {}
        self.cursor.execute('SELECT * FROM ingredient')
        elements = self.cursor.fetchall()
        for element in elements:
            name = element[3]
            q = element[4]
            if name in quantity_by_name:
                quantity_by_name[name] += q
            else:
                quantity_by_name[name] = q
        return quantity_by_name
    
    def check_missing_items(self):
        item_in = self.get_all_items()
        requirements = ingredients_requirements
        missing_items = []
        print(item_in)
        for item in requirements:
            if item not in item_in:
                missing_items.append([item, 0])
            else:
                if item_in[item] < requirements[item][0]:
                    missing_items.append([item, requirements[item][0] - item_in[item]])
        return missing_items

if __name__ == '__main__':
    data_manager = DataManager('../data/inventory.db')
    print(data_manager.check_missing_items())