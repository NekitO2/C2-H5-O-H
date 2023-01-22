import telebot 
import wikipedia 
 
bot = telebot.TeleBot('5891506134:AAHYfMnjRB6hAvuAOvQJYv_J7BEO1ytcKY8') 
wikipedia.set_lang('ru') 
 

@bot.message_handler(commands = ['help']) 
 
def send_help_message(message): 
    bot.send_message(message.chat.id, 'Отправь мне слово, я отправлю тебе статью Wikipedia') 
 
@bot.message_handler(content_types = ['text']) 
 

def send_message(message): 
    try: 
        article = wikipedia.page(message.text)
        bot.send_message(message.chat.id, f'Статья про: {article.title}')
        bot.send_message(message.chat.id, f'{article.content[:1000]}... ') 
        bot.send_message(message.chat.id, f'Ссылка на полную статью: {article.url}') 
    
    except: 
        
        bot.send_message(message.chat.id, 'Я не могу найти эту статью') 
 
bot.polling(non_stop = True)