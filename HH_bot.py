import json
# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater(token='583905412:AAGwYtlkfx0LxXfHue4IVZjKruHhzDohyB8') # Токен API к Telegram
dispatcher = updater.dispatcher


def get_fil_info(id):

    response = ""
    with open('kontacts.json', 'r', encoding='UTF-8') as info:
        data = json.loads(info.read())
        for i in data[id]:
            response = response + data[id][i] + '\n'
    return response


# Обработка команд
def startCommand(bot, update):
    greeting = """
Приветствую!
Я официальный Телеграм бот от ГАО ЯО МФЦ.
Запущен в тестовом режиме.
Информация по какому филиалу вам нужна?
Введите номер для:
1 - Ленинский р-н
2 - Кировский р-н
3 - Дзержинский р-н
4 - Заволжский р-н 
    """
    bot.send_message(chat_id=update.message.chat_id, text=greeting)


def textMessage(bot, update):
    # Ведение лога вопросов к боту
    with open('input.txt', 'a') as f_log:
        f_log.write('-'*5 + 'new message' + '-'*5+'\n')
        f_log.write(update.message.text+'\n')
        # f_log.write(update.message.location + '\n')

    user_res = update.message.text
    # print(user_res, type(user_res))
    # print(user_res.isdigit())
    try:
        if user_res in ["0", "1", "2", "3", "4"]:
            response = get_fil_info(int(user_res)-1)
        else:
            response = 'Получил Ваше сообщение: ' + update.message.text
    except:
        response = "error!"
    bot.send_message(chat_id=update.message.chat_id, text=response)


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

# Начинаем поиск обновлений
updater.start_polling(clean=True)

# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
