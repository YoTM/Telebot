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
