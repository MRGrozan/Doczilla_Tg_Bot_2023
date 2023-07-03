from telebot import types

key_admin = types.InlineKeyboardMarkup()
but_administration = (types.InlineKeyboardButton(text='Пользователи', callback_data='admin'))
but_back = (types.InlineKeyboardButton(text='Назад', callback_data='back1'))
key_admin.row(but_administration, but_back)
