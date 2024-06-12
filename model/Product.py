import sqlite3
from tkinter import messagebox
from app.connection import Database
database = Database()

class Product:
    def __init__(self):
        self.table()

    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS products (
                                        id INTEGER PRIMARY KEY,
                                        product_name TEXT NOT NULL,
                                        category TEXT NOT NULL,
                                        quantity INTEGER NOT NULL,
                                        sall_price REAL NOT NULL,
                                        cost_price REAL NOT NULL
                                    )''')

    def create(values):
            query = 'INSERT INTO products (product_name, category, quantity, sall_price, cost_price) VALUES (?,?,?,?,?)'
            params = (values[0], values[1], values[2], values[3], values[4])
            result = database.insert(query, params)
            if result > 0:
                return result
            else:
                return None

    def all(self):
        query = ("SELECT * FROM products")
        result = database.select(query)
        if not len(result) == 0:
            return result
        else:
            return None
        
    def chack(name):
            query = 'SELECT * FROM products WHERE product_name=?'
            params = (name,)
            result = database.onselect(query,params)
            if not len(result) == 0:
                return result
            else:
                return None

