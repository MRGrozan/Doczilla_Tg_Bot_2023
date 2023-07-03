from keyboa.keyboards import keyboa_maker
from database import get_users
get_users_bd = get_users.get_all_users()
print (get_users_bd)
users = []
def chec_users():
    users.clear()
    for i in get_users.get_all_users():
        print(i[0]+' '+i[1])
        users.append({f"{i[0]}": f"{i[1]}"})
    print (get_users_bd)

    kb_fruits = keyboa_maker(items=users, copy_text_to_callback=True,items_in_row=2)
    return kb_fruits