import requests
import json
from config import API_TOKEN, currencies

class Converter:
    def __init__(self):
        pass
    @staticmethod
    def get_price(meseg):
        if len(meseg) > 3 or len(meseg) < 3:
            raise ConvertException('Не совпадает количество параметров!')
        base, quote, amount = list(meseg)
        if base.upper() not in currencies or quote.upper() not in currencies:
            raise ConvertException('Неизвестные валюты!')
        if base.upper() == quote.upper():
            raise ConvertException('Вы ввели одинаковые валюты!')
        if float(amount) <= 0:
            raise ConvertException('Количество валюты < или = 0!')

        couples = base.upper()+quote.upper()
        response = requests.get(f'https://currate.ru/api/?get=rates&pairs={couples}&key={API_TOKEN}')
        answer = float(json.loads(response.text)['data'][couples]) * float(amount)
        return answer

class ConvertException(Exception):
    pass