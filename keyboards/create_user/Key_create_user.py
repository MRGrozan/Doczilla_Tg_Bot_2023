from telebot import types

key_create = types.InlineKeyboardMarkup()
but_proffesional = (types.InlineKeyboardButton(text='Профессиональное создание', callback_data='profi'))
but_standat = (types.InlineKeyboardButton(text='Стандатрное создание', callback_data='standart'))
but_back = (types.InlineKeyboardButton(text='Назад', callback_data='back1'))
key_create.row(but_proffesional)
key_create.row(but_standat)
key_create.row(but_back)