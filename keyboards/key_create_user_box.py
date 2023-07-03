from telebot import types


key_main_all = types.ReplyKeyboardMarkup(resize_keyboard=True)
but_demo = types.KeyboardButton('Демо')
but_dev = types.KeyboardButton('Дев')
but_test = types.KeyboardButton('Тест')
but_hr = types.KeyboardButton('HR')
key_main_all.row(but_demo,but_dev,but_test)
key_main_all.add(but_hr)
