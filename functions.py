from connection import Database
import os

def get_db_path():
    if os.path.exists('/app/choco.db'):
        return '/app/choco.db'  
    else:
        return '/yourPath/yourDatabase.db'  

def add_flavor(name, seasonal):
    with Database(get_db_path()) as con:
        cursor = con.cursor()
        cursor.execute('INSERT INTO flavors (name, seasonal) VALUES (?, ?)', (name, seasonal))
        con.commit()

def view_flavors():
    with Database(get_db_path()) as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM flavors')
        return cursor.fetchall()

def delete_flavor(flavor_id):
    with Database(get_db_path()) as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM flavors WHERE flav_id = ?', (flavor_id,))
        con.commit()

def add_ingredient(name, quantity):
    with Database(get_db_path()) as con:
        cursor = con.cursor()
        cursor.execute('INSERT INTO ingredients (name, quantity) VALUES (?, ?)', (name, quantity))
        con.commit()

def view_ingredients():
    with Database(get_db_path()) as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM ingredients')
        return cursor.fetchall()

def delete_ingredient(ingredient_id):
    with Database(get_db_path()) as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM ingredients WHERE ing_id = ?', (ingredient_id,))
        con.commit()

def add_suggestion(customer_name, flavor_suggestion, allergy_concern):
    with Database(get_db_path()) as con:
        cursor = con.cursor()
        cursor.execute('INSERT INTO suggestions (cust_name, flav_sugg, all_con) VALUES (?, ?, ?)', 
                       (customer_name, flavor_suggestion, allergy_concern))
        con.commit()

def view_suggestions():
    with Database(get_db_path()) as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM suggestions')
        return cursor.fetchall()

def delete_suggestion(suggestion_id):
    with Database(get_db_path()) as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM suggestions WHERE sugg_id = ?', (suggestion_id,))
        con.commit()
