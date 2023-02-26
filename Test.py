import requests
import telebot
import time


bot = telebot.TeleBot('5891506134:AAHYfMnjRB6hAvuAOvQJYv_J7BEO1ytcKY8') 


def get_fiat():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    response.raise_for_status()
    valute = response.json()['Valute']
    euro = int(valute['EUR']['Value'])
    dollar = int(valute['USD']['Value'])
    belorussia_ruble = int(valute['BYN']['Value'])
    fynt_sterling = int(valute['GBP']['Value'])
    tenge = int(valute['KZT']['Value'])
    griven = int(valute['UAH']['Value'])

    return euro, dollar, belorussia_ruble, fynt_sterling, tenge, griven


def get_crypto():
    
    def get_price(valute):

        params = {
            'symbol': f'{valute}USDT'
        }
        response = requests.get('https://api4.binance.com/api/v3/avgPrice', params=params)
        response.raise_for_status()
        return int((float((response.json()['price']))) * 72) 
    
    
    bitcoin = get_price('BTC')
    
    ethereum = get_price('ETH')

    bnb = get_price('BNB')

    ada = get_price('ADA')

    poligon = get_price('MATIC')
    
    return bitcoin, ethereum, bnb, ada, poligon


@bot.message_handler(commands=['start'])
def send_start_message(message):
    
    bot.send_message(message.chat.id, 'Введите интервал отправления сообщения о курсах валют в секундах')

@bot.message_handler(content_types = ['text'])
def send_message(message):
    
    while 1:
        try:
        
        
            euro_price, dollar_price, belorussia_ruble_price, fynt_sterling_price, tenge_price, griven_price = get_fiat()
            bitcoin_price, ethereum_price, bnb_price, ada_price, poligon_price = get_crypto()
            time.sleep(int(message.text))
            bot.send_message(message.chat.id, f'Евро - {euro_price} рублей\nДоллар - {dollar_price} рублей\nБелорусский рубль - {belorussia_ruble_price} рублей\nФунт стерлинг - {fynt_sterling_price} рублей\nКазахский тенге - {tenge_price} рублей\nГривен - {griven_price} рублей\n\n\nBitcoin - {bitcoin_price} рублей\nEthereum - {ethereum_price} рублей\nBNB - {bnb_price} рублей\nADA - {ada_price} рублей\nPoligon - {poligon_price} рублей')

        except:

            bot.send_message(message.chat.id, 'Проверьте сообщение')
            bot.send_message(message.chat.id, 'Введите интервал отправления сообщения о курсах валют в секундах')
            break

bot.polling(non_stop=True)  
