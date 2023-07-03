from keyboards.calendar import key_calendar
from configs import tg
import telebot
from database import add_new_user, check_permission,get_user_info
from configs import log
from keyboards import key_menu,key_admin_users,key_user_administration, key_admin, key_utils
from keyboards.create_user import Key_create_user
from keyboards.admin_dz import get_users
from generate_dictionary import send_file
from statistic import create_list
log.create_log_files()

bot = telebot.TeleBot(tg.TOKEN)
#bot.send_chat_action(chat_id=chat_id, action=t)

@bot.callback_query_handler(func=lambda call: True)
def calback(call):
    if call.data == "mouth":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери месяц',reply_markup=key_calendar.key_mouth)
    elif call.data == "mouth_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери месяц',reply_markup=key_calendar.key_mouth_end)
    elif call.data == "january":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату{call.from_user.id}',reply_markup=key_calendar.key_january)
        create_list.time_start[call.from_user.id] = {'mouth': 1}

        print(create_list.time_start)
    elif call.data == "february":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_february)
    elif call.data == "march":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_march)
    elif call.data == "april":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_april)
    elif call.data == "may":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_may)
    elif call.data == "june":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_june)
    elif call.data == "july":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_july)
    elif call.data == "august":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_august)
    elif call.data == "september":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_september)
    elif call.data == "october":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_october)
    elif call.data == "november":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_november)
    elif call.data == "december":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери начальную дату',reply_markup=key_calendar.key_december)

    elif call.data == "january_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        create_list.time_end[call.from_user.id] = {'mouth': 1}
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_january)
    elif call.data == "february_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_february)
    elif call.data == "march_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_march)
    elif call.data == "april_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_april)
    elif call.data == "may_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_may)
    elif call.data == "june_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_june)
    elif call.data == "july_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_july)
    elif call.data == "august_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_august)
    elif call.data == "september_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_september)
    elif call.data == "october_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_october)
    elif call.data == "november_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_november)
    elif call.data == "december_end":
        bot.delete_message(call.message.chat.id,call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату',reply_markup=key_calendar.key_december)
    elif call.data == "pass":
        pass
    elif call.data == "back":
        bot.send_message(call.message.chat.id, f'Список пользователей:',reply_markup=key_admin_users.chec_users())
    elif call.data == "administration":
        bot.send_message(call.message.chat.id, f'Выбери действие',reply_markup=key_user_administration.key_administration)
    elif call.data == "banned":
        bot.send_message(call.message.chat.id, f'Пользователь забанен!')
    elif call.data == "up":
        bot.send_message(call.message.chat.id, f'Вы повыстили пользователя')
    elif call.data == "down":
        bot.send_message(call.message.chat.id, f'Вы понизили пользователя')
    elif call.data == "admin":
        bot.send_message(call.message.chat.id, f'Список пользователей:',reply_markup=key_admin_users.chec_users())
    elif len(call.data) >= 30:
        print(call.data)
    elif len(call.data) == 2:
        print(call.data)
        create_list.time_start[call.from_user.id]['number'] = call.data
        print(create_list.time_start)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, f'Выбери конечную дату', reply_markup=key_calendar.key_january_end)
    elif len(call.data) == 3:
        print(call.data)

    elif len(call.data) == 6:
        create_list.time_end[call.from_user.id] = {'number': call.data}
        print('end'+call.data)
        print(create_list.time_start,' ', create_list.time_end)
    else:

        bot.send_message(call.message.chat.id, f'Информация о пользователе:\n'
                                               f'Логин: {get_user_info.get_user_info(call.data)[0]}\n'
                                               f'Идентификатор: {get_user_info.get_user_info(call.data)[1]}\n'
                                               f'Статус: {get_user_info.get_user_info(call.data)[2]}\n'
                                               f'Забанен: {get_user_info.get_user_info(call.data)[4]}\n'
                                               f'Уведомления: {get_user_info.get_user_info(call.data)[5]}\n',reply_markup=key_user_administration.key_user_administration)

@bot.message_handler(commands=['start'])
def start_bot(message):
    if add_new_user.add_user(message.from_user.id, message.from_user.username) == '0':
        bot.send_message(message.chat.id,'Извини, моя база данных дала сбой, зайди позже😔')

    else:
        # "Печатает...."
       # bot.send_message(message.chat.id, 'test',reply_markup=key_calendar.key_january)
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, f'Привет {message.from_user.username}!\n'
                                          f'Рад снова видеть тебя ☺️\n'
                                          f'Для того чтобы посмотреть мои возможности тыкай\n'
                                          f'👉/menu👈\n'
                                          f'А ещё я обновился, если интересно посмотри, что поменялось\n'
                                          f'тык👉/update👈',reply_markup=key_calendar.key_january)
#

@bot.message_handler(commands=['menu'])
def main(message):
    if check_permission.get_permission(message.from_user.id) == 'guest':
        bot.send_message(message.chat.id, f'К сожалению, ваш статус гость\n'
                                          f'Мне запрещено предоставлять какую либо информацию, пользователям вашего статуса \n'
                                          f'Для того, чтобы повысить свой статус обратитесь к администратору или введите код доступа\n')
    elif check_permission.get_permission(message.from_user.id) == 'user':
        bot.send_message(message.chat.id, f'Добро пожаловать в систему!\n'
                                          f'Ваш статус: Пользователь \n'
                                          f'Некоторые функции могут быть недоступны',reply_markup=key_menu.key_main_user)
    elif check_permission.get_permission(message.from_user.id) == 'expert':
        bot.send_message(message.chat.id, f'Добро пожаловать в систему!\n '
                                          f'Ваш статус: Модератор \n'
                                          f'Некоторые функции могут быть недоступны',reply_markup=key_menu.key_main_expert)
    elif check_permission.get_permission(message.from_user.id) == 'administrator':
        bot.send_message(message.chat.id, f'Добро пожаловать в систему!\n '
                                          f'Ваш статус: Администратор \n'
                                          f'Вы имеете полный доступ ',reply_markup=key_menu.key_main_all)
    else:
        bot.send_message(message.chat.id, f'Произошло что-то странное, я не смог определить твой статус🧐\n'
                                          f'Ты уж не обижайся, но мне придется тебя заблокировать\n'
                                          f'Я отправил о тебе данные администратору, если с твоим аккаунтом все хорошо, то он разблокирует тебя')


        bot.send_message(message.chat.id, f'Вы были заблокированы системой!\n'
                                          f'Срок: Бессрочно\n')


@bot.message_handler(content_types=['text'], func=lambda call: True)
def condition(message):
    if message.text == '⚙️Администрирование':
        bot.send_message(message.chat.id, f'Админка!\n',reply_markup=key_admin.key_admin)
    elif message.text == 'Дополнительно':
        bot.send_message(message.chat.id, f'Выбери действие\n',reply_markup=key_utils.key_utils)
    elif message.text == 'Управление пользователями':
        bot.send_message(message.chat.id, f'Выбери действие\n',reply_markup=get_users.key_get_users())
    elif message.text == 'Создать УЗ':
        bot.send_message(message.chat.id, f'Выбери действие\n',reply_markup=Key_create_user.key_create)
    elif message.text == '⚙️Создать справочник':
        bot.send_message(message.chat.id,
                         'Для корректной работы необходимо загрузить xlsx файл, в котором название колонок находится строго в первой строчке.\n'
                         'Для корректного определения типа колонки необходимо:\n'
                         ' 1 - На второю строчку поместить данные (текст, число, дата)\n'
                         ' 2 - Установить для колонок таблицы соответствующий тип ')

        msg = bot.send_message(message.chat.id,
                               '📲 Отправьте файл')
        bot.register_next_step_handler(msg, send_file.send_xlsx)
    elif message.text == 'Статистика📈':
        bot.send_message(message.chat.id, f'Выбери начальную дату', reply_markup=key_calendar.key_mouth)
        create_list.time_start[message.from_user.id] = ''
        create_list.time_end[message.from_user.id] = ''
        print(create_list.time_start)



while True:
    try:
        print('Бот запустился без ошибок!')
        bot.polling(none_stop=True)
    except Exception as e:
        print('Ошибка на стороне бота:', e)