import requests


class Bot:
    def __init__(self, token):
        self.token = token
        self.api = f'https://api.telegram.org/bot{token}/'

    def send_message(self, chat_id, text):
        '''Отправка сообщения'''
        params = {
            'chat_id': chat_id,
            'text': text,
        }
        method = 'sendMessage'
        response = requests.post(self.api + method, params).json()
        return response

    def send_photo(self, chat_id, file, text):
        '''Отправка скриншота'''
        data = {
            'chat_id': chat_id,
            'caption': text
        }
        files = {
            'photo': open(file, 'rb'),
        }
        method = 'sendPhoto'
        response = requests.post(
                        self.api + method,
                        data=data,
                        files=files
        ).json()
        return response
