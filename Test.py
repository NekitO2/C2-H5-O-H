from random import randint 
import requests 
import telebot 
 
bot = telebot.TeleBot('5891506134:AAHYfMnjRB6hAvuAOvQJYv_J7BEO1ytcKY8') 
 
def get_images(number): 
 
    response = requests.get('https://api.spacexdata.com/v3/launches') 
 
    response.raise_for_status() 
 
    
    return  [response.json()[number]['links']['flickr_images'], response.json()[number]['rocket']['rocket_name'], response.json()[number]['mission_name'], response.json()[number]['rocket']['rocket_type'], response.json()[number]['flight_number']]  
    
 
 
@bot.message_handler(commands = ['start']) 
def send_start_message(message): 
    bot.send_message(message.chat.id, 'Привет! Отправь мне число от 1 до 100') 
     
   
@bot.message_handler(content_types = ['text'])

def send_images(message):


    try:
    
        list = get_images(int(message.text)) 
        # list = get_images(20) 

        bot.send_message(message.chat.id, f'Имя корабля: {list[1]}') 
        bot.send_message(message.chat.id, f'Тип ракеты: {list[3]}')
        bot.send_message(message.chat.id, f'Имя миссии: {list[2]}')
        bot.send_message(message.chat.id, f'Количество полётов: {list[4]}')
        
        if len(list[0]) > 0: 
            for images in list[0]: 
                bot.send_message(message.chat.id, images) 
        else: 
            bot.send_message(message.chat.id, 'Отправь другое число, тут пусто или нет изображений\n.·´¯`(>▂<)´¯`·. ') 

    except:
    
        bot.send_message(message.chat.id, 'Повторяю: введи число от 1 до 100! ') 
 
bot.polling(non_stop = True)