import requests
import json
from configs.dz import url
from get_session import get_session


def create_user():
    data = {
        "request": "org.zenframework.z8.server.base.table.system.view.UserView",
        "action": "create",
        "data": "[{'recordId':'00000000-0000-0000-0000-000000000000'}]",
        "session": get_session.get_session(url)
    }
    res = requests.post(url, data=data, timeout=20)
    print(res.text)


create_user()