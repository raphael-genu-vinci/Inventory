import tkinter as tk
from data_manager import DataManager

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inventory Manager")
        self.root.geometry("1200x800")
        self.root.resizable(False, False)

        self.ingredient_id_label = tk.Label(self.root, text="Ingredient ID:")
        self.ingredient_id_label.pack()

    

    def run(self):
        self.init_widgets()
        self.root.mainloop()

if __name__ == '__main__':
    gui = GUI()
    gui.run()
