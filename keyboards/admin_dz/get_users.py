import requests
import json
from keyboa.keyboards import keyboa_maker
from configs.dz import url
from get_session import get_session
message = []
def get_users():
        message.clear()
        data = {
            "request": "org.zenframework.z8.server.base.table.system.view.UserView",
            "action": "read",
            "limit": "99999999",
            "sort": '[{"property":"login","direction":"asc"}]',
            "session": get_session.get_session(url)
        }
        res = requests.post(url, data=data, timeout=20)
        print(json.loads(res.text)['data'])
        for i in json.loads(res.text)['data']:
            message.append({f"{i['login']}": f"{str(i['recordId'])}"})
        else:
           print(message)

       # data = {
       #     "request": "org.zenframework.z8.server.base.table.system.view.UserView",
       #     "action": "read",
       #     "limit": "99999999",
       #     "fields": '["user.login","userRoles.role.name","userRoles.userId"]',
       #     "query": "userRoles",
       #     "session": get_session.get_session(url)
       # }
       # res = requests.post(url, data=data, timeout=20)
       # print(json.loads(res.text)['data'])
       # for i in json.loads(res.text)['data']:
       #     message += f"login: {i['login']}"+'\nbanned: '+f"{i['banned']}"+'\nchangePassword: '+f"{i['changePassword']}"+'\nrecordId: '+f"{i['recordId']}\n\n"
       # else:
       #    print(message)
#

def key_get_users():
    get_users()
    key_users = keyboa_maker(items=message, copy_text_to_callback=True, items_in_row=2)
    return key_users

