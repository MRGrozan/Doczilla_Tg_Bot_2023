from telebot import types


key_utils = types.ReplyKeyboardMarkup(resize_keyboard=True)
but_create_user = types.KeyboardButton('Создать УЗ')
but_statistic = types.KeyboardButton('Статистика📈')
but_structure = types.KeyboardButton('Получить структуру')
but_users = types.KeyboardButton('Управление пользователями')
but_generate_dictionary = types.KeyboardButton('⚙️Создать справочник')



key_utils.row(but_create_user,but_statistic,but_generate_dictionary)
key_utils.add(but_structure,but_users)


