import requests

url = "https://api.telegram.org/bot583905412:AAGwYtlkfx0LxXfHue4IVZjKruHhzDohyB8/"


def get_updates_json(request):
    """
        Получаем все обновления за последние 24 часа
    """
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    """
        Получаем последнее обновление
    """
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    """
        Ф-я достаёт идентификатор чата из обновления
    """
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    """
        Ф-я отправки сообщения
    """
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url)))
send_mess(chat_id, 'Your message goes here')
