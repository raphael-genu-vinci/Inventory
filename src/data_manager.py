import sqlite3
import os 
import datetime
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
        """
        Adds an item to the database.
        
        Parameters:
            ingredient_id (int): The ID of the ingredient.
            type (str): The type of the ingredient.
            name (str): The name of the ingredient.
            quantity (float): The quantity of the ingredient.
            expiration_date (datetime.date): The expiration date of the ingredient.
            in_date (datetime.date): The date the ingredient was added.

        Raises:
            Exception: If there is an error while adding the item.
        """
        try :
            self.cursor.execute(
            'INSERT INTO ingredient (ingredient_id, type, name, quantity, in_date, expiration_date) VALUES (?, ?, ?, ?, ?, ?)',
            (ingredient_id, type, name, quantity, in_date, expiration_date)
            )
            self.connection.commit()
        except Exception as e:
            print("Error while adding item : ", e)

    def delete_item(self, id):
        """
        Deletes an item from the database.

        Parameters:
            id (int): The ID of the item to be deleted.
        """
        try :
            self.cursor.execute('DELETE FROM ingredient WHERE id = ?', (id,))
            self.connection.commit()
        except Exception as e:
            print("Error while deleting item : ", e)

    def get_all_items(self):
        """
        Get all items from the database and calculate the total quantity of each item.
        Returns:
            quantity_by_name (dict): A dictionary with the total quantity of each item indexed by name.
        """
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
        """
        Check for missing items in the inventory.

        This function compares the items in the inventory with the required items and returns a list of missing items.
        It iterates over the requirements dictionary and checks if each item is present in the inventory.
        If an item is missing, it calculates the difference between the required quantity and the quantity in the inventory
        and appends it to the missing_items list.

        Returns:
            missing_items (list): A list of missing items. Each item in the list is a list containing the item name and the
            difference between the required quantity and the quantity in the inventory.
        """
        item_in = self.get_all_items()
        requirements = ingredients_requirements
        missing_items = []
        for item in requirements:
            if item not in item_in:
                missing_items.append([item, requirements[item][0] - item_in[item]])
            else:
                if item_in[item] < requirements[item][0]:
                    missing_items.append([item, requirements[item][0] - item_in[item]])
        return missing_items
    
    def check_expired_items(self):
        """
        Check for expired items in the database and delete them. Returns the list of expired items.
        """
        today = datetime.date.today()
        print(today)
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM ingredient WHERE expiration_date < ?', (today,))
            expired_items = cursor.fetchall()
        for item in expired_items:
            self.delete_item(item[0])
        return expired_items
    
    def close(self):
        """
        Closes the connection to the database.
        """
        self.connection.close()

        