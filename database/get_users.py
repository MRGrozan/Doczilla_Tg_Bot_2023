import sqlite3

def get_all_users():
    connect = sqlite3.connect('database/doczilla.db')
    cursor = connect.cursor()
    cursor.execute(f"""SELECT user_name, user_id FROM users;""")
    data = cursor.fetchall()
    connect.commit()
    return list(data)
