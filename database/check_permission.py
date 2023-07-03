import sqlite3

def get_permission(user_id):
    connect = sqlite3.connect('database/doczilla.db')
    cursor = connect.cursor()
    cursor.execute(f"""SELECT permission FROM users WHERE (user_id = {user_id});""")
    data = cursor.fetchone()
    connect.commit()
    return data[0]

def give_permission(user_id):
    connect = sqlite3.connect('database/doczilla.db')
    cursor = connect.cursor()
    cursor.execute(f"""SELECT permission FROM users WHERE (user_id = {user_id});""")
    data = cursor.fetchone()
    connect.commit()
    return data[0]