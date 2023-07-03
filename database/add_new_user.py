import sqlite3
from loguru import logger
from configs import log

log.create_log_files()

def add_user(user_id,user_name):
    try:
        logger.info(f'[database] Пользователь: [[ {user_id} {user_name} ]] - Открыл БД')
        connect = sqlite3.connect('database/doczilla.db')
        cursor = connect.cursor()
        cursor.execute(f"""SELECT user_id FROM users WHERE (user_id = {user_id});""")
        data = cursor.fetchone()
        connect.commit()
        if data is None:
            logger.info(f'[database] Пользователь: {user_id} {user_name} ]] - Не найден в БД')
            connect = sqlite3.connect('database/doczilla.db')
            cursor = connect.cursor()
            cursor.execute(f"""INSERT INTO users (user_name, user_id, permission, banned,notification,old)
                                       VALUES('{user_name}','{user_id}','guest','false','true','true');""")
            logger.info(f'[database] Пользователь: [[ {user_id} {user_name} ]] - Произошла запись пользователя в БД')
            connect.commit()
            logger.info(f'[database] Пользователь: [[ {user_id} {user_name} ]] - Подключение к БД закрылось')
            return '1'
    except:
        logger.exception('[database]')
        return '0'