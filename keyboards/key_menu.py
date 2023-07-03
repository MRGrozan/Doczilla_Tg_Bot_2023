from telebot import types


key_main_all = types.ReplyKeyboardMarkup(resize_keyboard=True)
but_builds = types.KeyboardButton('🧱Сборки')
but_admin = types.KeyboardButton('⚙️Администрирование')
#but_generate_dictionary = types.KeyboardButton('⚙️Создать справочник')
but_get_utils = types.KeyboardButton('Дополнительно')


key_main_all.row(but_builds,but_get_utils)
key_main_all.add(but_admin)

key_main_expert = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_main_expert.row(but_builds,but_get_utils)



key_main_user = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_main_user.row(but_builds,but_get_utils)