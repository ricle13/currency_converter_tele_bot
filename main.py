import telebot
from extensions import Converter, ConvertException
from config import TELE_TOKEN, GREATINGS, HELP, VALUES, currencies

bot = telebot.TeleBot(TELE_TOKEN)

@bot.message_handler(commands = ['start'])
def start(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id,
                     text = GREATINGS,
                     parse_mode = 'html')
    bot.send_message(chat_id = message.chat.id,
                     text = HELP,
                     parse_mode = 'html')

@bot.message_handler(commands = ['help'])
def help(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id,
                     text = HELP,
                     parse_mode = 'html')

@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
    bot.send_message(chat_id = message.chat.id,
                     text = VALUES,
                     parse_mode = 'html')

@bot.message_handler()
def convert(message: telebot.types.Message):
    try:
        mes = message.text.split()
        if len(mes) > 3 or len(mes) < 3:
            raise ConvertException('Не совпадает количество параметров!')
        base, quote, amount = list(mes)
        if base.upper() not in currencies or quote.upper() not in currencies:
            raise ConvertException('Неизвестные валюты!')
        if base.upper() == quote.upper():
            raise ConvertException('Вы ввели одинаковые валюты!')
        if float(amount) <= 0:
            raise ConvertException('Количество валюты < или = 0!')
        answer = Converter.get_price(base = base, quote = quote, amount = amount)
    except ConvertException as e:
        bot.reply_to(message,f'Ошибка пользователя.\n {e}')
    except Exception as e:
        bot.reply_to(message,f'Что-то пошло не так.\n {e}')
    else:
        bot.send_message(chat_id = message.chat.id,
                         text = answer)

bot.polling()