import random
import time

import telebot
from telebot import types

bot = telebot.TeleBot('5891506134:AAHYfMnjRB6hAvuAOvQJYv_J7BEO1ytcKY8')
data = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Нахождение даты 

@bot.message_handler(commands=['start'])


def start(message):

    buttons = types.InlineKeyboardMarkup(row_width = 2) # Переменная, передающая параметры кнопки (клавиатуры)
    button1 = types.InlineKeyboardButton(text = "1", callback_data = '1') # Формирование текста кнопки(клавиатуры) и создание переменной, которая определяет дальнейшие действия
    button2 = types.InlineKeyboardButton(text = "2", callback_data = '2') # Формирование текста кнопки(клавиатуры) и создание переменной, которая определяет дальнейшие действия
    button3 = types.InlineKeyboardButton(text = "3", callback_data = '3') # Формирование текста кнопки(клавиатуры) и создание переменной, которая определяет дальнейшие действия
    button4 = types.InlineKeyboardButton(text = "4", callback_data = '4') # Формирование текста кнопки(клавиатуры) и создание переменной, которая определяет дальнейшие действия
    button5 = types.InlineKeyboardButton(text = "5", callback_data = '5') # Формирование текста кнопки(клавиатуры) и создание переменной, которая определяет дальнейшие действия
    button6 = types.InlineKeyboardButton(text = "6", callback_data = '6') # Формирование текста кнопки(клавиатуры) и создание переменной, которая определяет дальнейшие действия
    button7 = types.InlineKeyboardButton(text = "7", callback_data = '7') # Формирование текста кнопки(клавиатуры) и создание переменной, которая определяет дальнейшие действия
    button8 = types.InlineKeyboardButton(text = "8", callback_data = '8') # Формирование текста кнопки(клавиатуры) и создание переменной, которая определяет дальнейшие действия
    button9 = types.InlineKeyboardButton(text = "9", callback_data = '9') # Формирование текста кнопки(клавиатуры) и создание переменной, которая определяет дальнейшие действия
    button10 = types.InlineKeyboardButton(text = "10", callback_data = '10') # Формирование текста кнопки(клавиатуры) и создание переменной, которая определяет дальнейшие действия
    buttons.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10) # Вывод кнопки(клавиатуры)
    bot.send_message(message.chat.id, 'Выберите число', reply_markup=buttons) # Отправка сообщения и прикрепление к нему кнопки(клавиатуры)
    
@bot.callback_query_handler(func = lambda call: True) # Обработчик

def end(call):
    b = str(random.randint(1,10))
    if call.message:
        if call.data == '1':
            
            if call.data == b:
                bot.send_message(call.message.chat.id, 'Ты угадал (^人^)')

            else:
                bot.send_message(call.message.chat.id, 'Попробуй ещё раз （＞人＜)')
            
        elif call.data == '2':
            
            if call.data == b:
                bot.send_message(call.message.chat.id, 'Ты угадал (^人^)')

            else:
                bot.send_message(call.message.chat.id, 'Попробуй ещё раз （＞人＜)') 
    
        elif call.data == '3':
            
            if call.data == b:
                bot.send_message(call.message.chat.id, 'Ты угадал (^人^)')

            else:
                bot.send_message(call.message.chat.id, 'Попробуй ещё раз （＞人＜)')
            
        elif call.data == '4':
            
            if call.data == b:
                bot.send_message(call.message.chat.id, 'Ты угадал (^人^)')

            else:
                bot.send_message(call.message.chat.id, 'Попробуй ещё раз （＞人＜)') 
        
        elif call.data == '5':
            
            if call.data == b:
                bot.send_message(call.message.chat.id, 'Ты угадал (^人^)')

            else:
                bot.send_message(call.message.chat.id, 'Попробуй ещё раз （＞人＜)')
            
        elif call.data == '6':
            
            if call.data == b:
                bot.send_message(call.message.chat.id, 'Ты угадал (^人^)')

            else:
                bot.send_message(call.message.chat.id, 'Попробуй ещё раз （＞人＜)') 

        elif call.data == '7':
            
            if call.data == b:
                bot.send_message(call.message.chat.id, 'Ты угадал (^人^)')

            else:
                bot.send_message(call.message.chat.id, 'Попробуй ещё раз （＞人＜)')
            
        elif call.data == '8':
            
            if call.data == b:
                bot.send_message(call.message.chat.id, 'Ты угадал (^人^)')

            else:
                bot.send_message(call.message.chat.id, 'Попробуй ещё раз （＞人＜)') 

        elif call.data == '9':
            
            if call.data == b:
                bot.send_message(call.message.chat.id, 'Ты угадал (^人^)')

            else:
                bot.send_message(call.message.chat.id, 'Попробуй ещё раз （＞人＜)')
            
        elif call.data == '10':
            
            if call.data == b:
                bot.send_message(call.message.chat.id, 'Ты угадал (^人^)')

            else:
                bot.send_message(call.message.chat.id, 'Попробуй ещё раз （＞人＜)') 

    
    message = types.ReplyKeyboardMarkup(row_width = 1) # Переменная, передающая параметры клавиатуры
    button = types.KeyboardButton('/start') # Формирование текста кнопки(клавиатуры) 
    
    bot.send_message(call.message.chat.id, 'Повторить? ¯\_(ツ)_/¯',reply_markup=message) # Отправка сообщения
    bot.send_message(call.message.chat.id, f'Кстати, ты написал "{call.data}" в {data(call.message.date)}')

bot.polling(non_stop= True)

