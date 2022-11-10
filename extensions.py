import requests
import json
from config import API_TOKEN

class Converter:
    def __init__(self):
        pass
    @staticmethod
    def get_price(base, quote, amount):
        couples = base.upper()+quote.upper()
        response = requests.get(f'https://currate.ru/api/?get=rates&pairs={couples}&key={API_TOKEN}')
        answer = float(json.loads(response.text)['data'][couples]) * float(amount)
        return answer

class ConvertException(Exception):
    pass