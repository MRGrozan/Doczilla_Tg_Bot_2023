import requests
import json
from configs.dz import login_create_user,password_create_user

def get_session(url):
    try:
        data = {
            "request": 'signin',
            "login": login_create_user,
            "password": password_create_user
        }
        res = requests.post(url, data=data, timeout=20)
        session = json.loads(res.text)['user']['session']
        return session
    except:
        print("Ошибка авторизации")
