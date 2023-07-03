import sqlite3

def get_user_info(user_id):
    connect = sqlite3.connect('database/doczilla.db')
    cursor = connect.cursor()
    cursor.execute(f"""SELECT * FROM users WHERE user_id = {user_id}""")
    data = cursor.fetchone()
    connect.commit()
    print(data)
    return list(data)
