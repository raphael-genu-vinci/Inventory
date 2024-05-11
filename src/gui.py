import tkinter as tk
from data_manager import DataManager

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inventory Manager")
        self.root.geometry("1200x800")
        self.root.resizable(False, False)
        self.data_manager = DataManager('../data/inventory.db')
    

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    gui = GUI()
    gui.run()
