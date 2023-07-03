from configs import tg
import telebot
from generate_dictionary import gen_dictionary
bot = telebot.TeleBot(tg.TOKEN)





def send_xlsx(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        name_document = message.document.file_name

        with open(f"temp/xlsx/{name_document}", 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, '💾я получил файл')
        paht_file = f"temp/xlsx/{name_document}"
        gen_dictionary.generate(message,paht_file)
    except Exception as e:
        bot.send_message(message.chat.id,
                         f'🧐хм.... похоже этот файл мне не подходит {e}')