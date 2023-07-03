from telebot import types

key_user_administration = types.InlineKeyboardMarkup()
but_administration = (types.InlineKeyboardButton(text='Управление', callback_data='administration'))
but_back = (types.InlineKeyboardButton(text='Назад', callback_data='back'))
key_user_administration.row(but_administration, but_back)


key_administration = types.InlineKeyboardMarkup()
but_ban = (types.InlineKeyboardButton(text='Заблокировать', callback_data='banned'))
but_unban = (types.InlineKeyboardButton(text='Разблокировать', callback_data='unbanned'))
but_up_admin = (types.InlineKeyboardButton(text='Повысить до администратора', callback_data='up_admin'))
but_up_expert = (types.InlineKeyboardButton(text='Повысить до эксперта', callback_data='up_expert'))
but_down_expert = (types.InlineKeyboardButton(text='понизить до эксперта', callback_data='down_expert'))
but_down_user = (types.InlineKeyboardButton(text='понизить до пользователя', callback_data='down_user'))
but_down = (types.InlineKeyboardButton(text='Забрать все права', callback_data='down'))
key_administration.row(but_ban,but_unban)
key_administration.add(but_up_admin, but_up_expert)
key_administration.add(but_down_expert, but_down_user)
key_administration.add(but_down,but_back)
