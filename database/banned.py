import sqlite3

def add_banned(user_id):
    connect = sqlite3.connect('database/doczilla.db')
    cursor = connect.cursor()
    cursor.execute(f"""UPDATE users SET banned = 'true' WHERE (id = {user_id} );""")
    connect.commit()

def dell_banned(user_id):
    connect = sqlite3.connect('database/doczilla.db')
    cursor = connect.cursor()
    cursor.execute(f"""UPDATE users SET banned = 'false' WHERE (id = {user_id} );""")
    connect.commit()
