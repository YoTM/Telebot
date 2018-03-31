# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='583905412:AAGwYtlkfx0LxXfHue4IVZjKruHhzDohyB8') # Токен API к Telegram
dispatcher = updater.dispatcher

# Обработка команд
def startCommand(bot, update):
    greeting = """

        Приветствую!
    Я официальный Телеграм бот от ГАО ЯО МФЦ.
    Запущен в тестовом режиме.
    Понимаю команды:
    Раз -
    Два -
    Три -

    """
    bot.send_message(chat_id=update.message.chat_id, text=greeting)


def textMessage(bot, update):
    with open('input.txt', 'a') as f_log:
        f_log.write('-'*5 + 'new message' + '-'*5+'\n')
        f_log.write(update.message.text+'\n')
    if update.message.text == 'загран паспорт':
        response = """
        Способы подачи заявки:
            Лично
            Через законного представителя
            Через МФЦ
        Способы получения результата:
            Лично
            Через законного представителя
            Через МФЦ
        Стоимость и порядок оплаты
            Вид платежа:
                Государственная пошлина
            Стоимость:
                2000.0
        """
    else:
        response = 'Получил Ваше сообщение: ' + update.message.text
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
