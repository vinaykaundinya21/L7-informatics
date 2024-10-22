import sqlite3
import os

class DBConnection:
    def __init__(self, db_path):
        self.db_path = db_path

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

def initialize(connection):
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chocolate_flavors (
        flavor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_name TEXT NOT NULL,
        is_seasonal BOOLEAN NOT NULL
    )                        
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredient_stock (
        ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient_name TEXT NOT NULL,
        available_quantity INTEGER NOT NULL
    )                        
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_feedback (
        feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        flavor_suggestion TEXT,
        allergy_info TEXT
    )                        
    ''')

    connection.commit()
