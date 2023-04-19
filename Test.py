# coding=UTF-8
import telebot
from telebot import types
from time import sleep
from environs import Env

bot = telebot.TeleBot('superpupermegaultratoken123')   
number_of_incorrect_answers_given = 0   
def send_message_about_the_incorrect_choice(call, markup):

    global number_of_incorrect_answers_given, return_vars
    number_of_incorrect_answers_given += 1
    print(number_of_incorrect_answers_given)
    bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = f'Подумайте ещё\n\nЧисло данных некорректных ответов: {number_of_incorrect_answers_given}', reply_markup = markup)

markup_question_1 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('12.04.1961', callback_data = '12.04.1961')
button2 = types.InlineKeyboardButton('04.10.1957', callback_data = '04.10.1957')
button3 = types.InlineKeyboardButton('16.07.1969', callback_data = '16.07.1969')
markup_question_1.add(button1, button2, button3)

markup_question_2 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('К. Э. Циолковский', callback_data = 'К. Э. Циолковский')
button2 = types.InlineKeyboardButton('Н. Е. Жуковский', callback_data = 'Н. Е. Жуковский')
button3 = types.InlineKeyboardButton('С. П. Королев', callback_data = 'С. П. Королев')
markup_question_2.add(button1, button2, button3)

markup_question_3 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Планета', callback_data = 'Планета')
button2 = types.InlineKeyboardButton('Небо', callback_data = 'Небо')
button3 = types.InlineKeyboardButton('Вселенная', callback_data = 'Вселенная')
markup_question_3.add(button1, button2, button3)

markup_question_4 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Космонавтика', callback_data = 'Космонавтика')
button2 = types.InlineKeyboardButton('Астрономия', callback_data = 'Астрономия')
button3 = types.InlineKeyboardButton('Астрология', callback_data = 'Астрология')
markup_question_4.add(button1, button2, button3)

markup_question_5 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('7', callback_data = '7')
button2 = types.InlineKeyboardButton('8', callback_data = '8')
button3 = types.InlineKeyboardButton('9', callback_data = '9')
markup_question_5.add(button1, button2, button3)

markup_question_6 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Сатурн', callback_data = 'Сатурн')
button2 = types.InlineKeyboardButton('Меркурий', callback_data = 'Меркурий')
button3 = types.InlineKeyboardButton('Юпитер', callback_data = 'Юпитер')
markup_question_6.add(button1, button2, button3)

markup_question_7 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Солнце', callback_data = 'Солнце(7)')
button2 = types.InlineKeyboardButton('Луна', callback_data = 'Луна')
button3 = types.InlineKeyboardButton('Комета Галлея', callback_data = 'Комета Галлея')
markup_question_7.add(button1, button2, button3)

markup_question_8 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Стрелка', callback_data = 'Стрелка')
button2 = types.InlineKeyboardButton('Белка', callback_data = 'Белка')
button3 = types.InlineKeyboardButton('Лайка', callback_data = 'Лайка')
markup_question_8.add(button1, button2, button3)

markup_question_9 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('108 минут', callback_data = '108 минут')
button2 = types.InlineKeyboardButton('20 минут', callback_data = '20 минут')
button3 = types.InlineKeyboardButton('45 минут', callback_data = '45 минут')
markup_question_9.add(button1, button2, button3)

markup_question_10 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Андриян Николаев', callback_data = 'Андриян Николаев')
button2 = types.InlineKeyboardButton('Валерий Быковский', callback_data = 'Валерий Быковский')
button3 = types.InlineKeyboardButton('Герман Титов', callback_data = 'Герман Титов')
markup_question_10.add(button1, button2, button3)

markup_question_11 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Восход', callback_data = 'Восход')
button2 = types.InlineKeyboardButton('Восток', callback_data = 'Восток')
button3 = types.InlineKeyboardButton('Союз', callback_data = 'Союз')
markup_question_11.add(button1, button2, button3)

markup_question_12 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Клен', callback_data = 'Клен')
button2 = types.InlineKeyboardButton('Кедр', callback_data = 'Кедр')
button3 = types.InlineKeyboardButton('Земля', callback_data = 'Земля')
markup_question_12.add(button1, button2, button3)

markup_question_13 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Алексей Леонов', callback_data = 'Алексей Леонов')
button2 = types.InlineKeyboardButton('Эдвард Уайт ', callback_data = 'Эдвард Уайт')
button3 = types.InlineKeyboardButton('Джон Янг', callback_data = 'Джон Янг')
markup_question_13.add(button1, button2, button3)

markup_question_14 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Валентина Терешкова', callback_data = 'Валентина Терешкова(14)')
button2 = types.InlineKeyboardButton('Салли Райд', callback_data = 'Салли Райд')
button3 = types.InlineKeyboardButton('Светлана Савицкая', callback_data = 'Светлана Савицкая')
markup_question_14.add(button1, button2, button3)

markup_question_15 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Викинг', callback_data = 'Викинг')
button2 = types.InlineKeyboardButton('Шаттл', callback_data = 'Шаттл')
button3 = types.InlineKeyboardButton('Пионер', callback_data = 'Пионер')
markup_question_15.add(button1, button2, button3)

markup_question_16 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Елена Кондакова', callback_data = 'Елена Кондакова')
button2 = types.InlineKeyboardButton('Валентина Терешкова', callback_data = 'Валентина Терешкова(16)')
button3 = types.InlineKeyboardButton('Пономарева Валентина', callback_data = 'Пономарева Валентина')
markup_question_16.add(button1, button2, button3)

markup_question_17 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Икар', callback_data = 'Икар')
button2 = types.InlineKeyboardButton('Геракл', callback_data = 'Геракл')
button3 = types.InlineKeyboardButton('Минотавр', callback_data = 'Минотавр')
markup_question_17.add(button1, button2, button3)

markup_question_18 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Сириус', callback_data = 'Сириус')
button2 = types.InlineKeyboardButton('Альдебаран', callback_data = 'Альдебаран')
button3 = types.InlineKeyboardButton('Солнце', callback_data = 'Солнце(18)')
markup_question_18.add(button1, button2, button3)

markup_question_19 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Круглая', callback_data = 'Круглая')
button2 = types.InlineKeyboardButton('Космическая', callback_data = 'Космическая')
button3 = types.InlineKeyboardButton('Блуждающая', callback_data = 'Блуждающая')
markup_question_19.add(button1, button2, button3)

markup_question_20 = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('Сатурн', callback_data = 'Сатурн')
button2 = types.InlineKeyboardButton('Марс', callback_data = 'Марс')
button3 = types.InlineKeyboardButton('Уран', callback_data = 'Уран')
markup_question_20.add(button1, button2, button3)

@bot.message_handler(commands = ['start'])

def send_start_message(message):
    global number_of_incorrect_answers_given
    number_of_incorrect_answers_given = 0
    markup_start = types.InlineKeyboardMarkup(row_width = 1)
    button = types.InlineKeyboardButton(text = 'Старт викторины', callback_data = 'Start')
    markup_start.add(button)
    bot.send_message(message.chat.id, 'Здравствуй, дорогой товарищ! Если вы хотите расширить свой кругозор в области Космонавтики, то вы пришли по адресу!',reply_markup = markup_start)

@bot.callback_query_handler(func = lambda call: call.data == 'Start')

def send_question_1(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 1\n\nКогда был осуществлён первый полёт человека в космос?', reply_markup = markup_question_1)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_2')
 

def send_question_2(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 2\n\nКого считают "отцом космонавтики"?', reply_markup = markup_question_2)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_3')
 

def send_question_3(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 3\n\nЧто означает слово "космос"? ', reply_markup = markup_question_3)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_4')

def send_question_4(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 4\n\nКак называется наука о строении и развитии космических тел, их систем и вселенной в целом?', reply_markup = markup_question_4)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_5')

def send_question_5(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 5\n\nСколько планет в Солнечной системе?', reply_markup = markup_question_5)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_6')

def send_question_6(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 6\n\nКакая из планет самая большая?', reply_markup = markup_question_6)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_7')

def send_question_7(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 7\n\nКакое самое близкое к Земле космическое тело?', reply_markup = markup_question_7)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_8')

def send_question_8(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 8\n\nКак звали собаку, которая первой полетела в космос вместе с искусственным спутником земли?', reply_markup = markup_question_8)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_9')

def send_question_9(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 9\n\nСколько длился первый полет человека?', reply_markup = markup_question_9)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_10')

def send_question_10(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 10\n\nКто был дублером первого космонавта Земли Ю. А. Гагарина?', reply_markup = markup_question_10)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_11')

def send_question_11(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 11\n\nКак назывался космический корабль, на котором стартовал Ю.А. Гагарин?', reply_markup = markup_question_11)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_12')

def send_question_12(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 12\n\nКакой позывной был у Ю. А. Гагарина?', reply_markup = markup_question_12)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_13')

def send_question_13(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 13\n\nКто первым из космонавтов вышел в открытый космос?', reply_markup = markup_question_13)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_14')

def send_question_14(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 14\n\nКто из женщин-космонавтов впервые вышел в открытый космос?', reply_markup = markup_question_14)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_15')

def send_question_15(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 15\n\nКак назывался космический аппарат, покинувший в 1973 году Солнечную систему и сделавший цветные снимки Юпитера?', reply_markup = markup_question_15)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_16')

def send_question_16(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 16\n\nУ кого из космонавтов был позывной "Чайка"?', reply_markup = markup_question_16)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_17')

def send_question_17(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 17\n\nКто из героев древних мифов преодолел силу земного притяжения и полетел?', reply_markup = markup_question_17)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_18')

def send_question_18(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 18\n\nКакая ближайшая к нам звезда?', reply_markup = markup_question_18)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_19')

def send_question_19(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 19\n\nЧто в переводе на русский означает слово «планета»?', reply_markup = markup_question_19)

@bot.callback_query_handler(func = lambda call: call.data == 'Question_20')

def send_question_20(call):

    bot.send_message(call.message.chat.id, 'Вопрос: 20 Финальный 😃\n\nКакая из планет Солнечной системы имеет два спутника, названия которых на русский язык переводятся как «страх» и «ужас»?', reply_markup = markup_question_20)

@bot.callback_query_handler(func = lambda call: True)

def check_questions(call):
    
    try:
        if call.message:
            

            if call.data == '12.04.1961': 
        
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_2')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\n12 апреля 1961 года был совершён первый полёт человека в космос. Этим "счастливчиком" стал Юрий Алексеевич Гагарин(9.03.1934 - 27.03.1968). Ракета-носитель «Восток» с кораблём «Восток-1», на борту которого находился Гагарин, была запущена с космодрома Байконур, расположенного в Кызылординской области Казахской ССР. После 108 минут[5] полёта Гагарин успешно приземлился в Саратовской области, неподалёку от Энгельса.\n\n12 апреля 1961 года, день полёта Юрия Гагарина в космос, был объявлен праздником — Днём космонавтики. В честь первого космонавта Земли был переименован ряд населённых пунктов (включая его родной город — Гжатск), названы улицы и проспекты. В разных городах мира было установлено множество памятников Гагарину.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Гагарин,_Юрий_Алексеевич', reply_markup = markup)

            elif call.data == '04.10.1957': send_message_about_the_incorrect_choice(call, markup_question_1)

            elif call.data == '16.07.1969': send_message_about_the_incorrect_choice(call, markup_question_1)


            elif call.data == 'К. Э. Циолковский':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_3')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nВ своих научно-фантастических произведениях, будучи сторонником и пропагандистом идей освоения космического пространства, Циолковский(17.09.1857 - 19.09.1935) предлагал заселить космическое пространство с использованием орбитальных станций, выдвинул идеи космического лифта, поездов на воздушной подушке. Считал, что развитие жизни на одной из планет когда-нибудь достигнет такого могущества и совершенства, которое позволит преодолеть силы тяготения и распространить жизнь по всей Вселенной. Необходимым этапом к расселению человечества в Космосе он считал возвышение интеллектуалов и выведение человечества, лишённого страстей, но с великим разумом, который позволит осуществить «рациональное умиротворённое существование». Эта эзотерическая утопия Циолковского послужила ведущим стимулом для разработки оснований ракетно-космической техники.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Циолковский,_Константин_Эдуардович', reply_markup = markup)
            
            elif call.data == 'Н. Е. Жуковский': send_message_about_the_incorrect_choice(call, markup_question_2)
            
            elif call.data == 'С. П. Королев': send_message_about_the_incorrect_choice(call, markup_question_2)


            elif call.data == 'Вселенная':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_4')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nВселе́нная — не имеющее строгого определения понятие в астрономии и философии. Оно делится на две принципиально отличающиеся сущности: умозрительную (философскую) и материальную, доступную наблюдениям в настоящее время или в обозримом будущем. Если автор различает эти сущности, то, следуя традиции, первую называют Вселенной, а вторую — астрономической Вселенной или Метагалактикой\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Вселенная', reply_markup = markup)
            
            elif call.data == 'Небо': send_message_about_the_incorrect_choice(call, markup_question_3)
            
            elif call.data == 'Планета  ': send_message_about_the_incorrect_choice(call, markup_question_3)

            
            elif call.data == 'Астрономия':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_5')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nАстрономия — наука о Вселенной, изучающая расположение, движение, структуру, происхождение и развитие небесных тел (планет, звёзд, астероидов, и т. д.) и систем. В частности, астрономия изучает Солнце и другие звёзды, планеты Солнечной системы и их спутники, экзопланеты, астероиды, кометы, метеороиды, межпланетное вещество, межзвёздное вещество, пульсары, чёрные дыры, туманности, галактики и их скопления, квазары и многое другое\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Астрономия', reply_markup = markup)
            
            elif call.data == 'Небо': send_message_about_the_incorrect_choice(call, markup_question_4)
            
            elif call.data == 'Планета': send_message_about_the_incorrect_choice(call, markup_question_4)


            elif call.data == '8':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_6')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nСолнечная система — планетная система, включающая в себя центральную звезду Солнце и все естественные космические объекты на гелиоцентрических орбитах. Она сформировалась путём гравитационного сжатия газопылевого облака примерно 4,57 млрд лет назад\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Солнечная_система', reply_markup = markup)
            
            elif call.data == '7': send_message_about_the_incorrect_choice(call, markup_question_5)
            
            elif call.data == '9': send_message_about_the_incorrect_choice(call, markup_question_5)


            elif call.data == 'Юпитер':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_7')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nЮпитер — крупнейшая планета Солнечной системы, пятая по удалённости от Солнца. Наряду с Сатурном Юпитер классифицируется как газовый гигант.\nРяд атмосферных явлений на Юпитере: штормы, молнии, полярные сияния, — имеет масштабы, на порядки превосходящие земные. Примечательным образованием в атмосфере является Большое красное пятно — гигантский шторм, известный с XVII века.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Юпитер', reply_markup = markup)
            
            elif call.data == 'Меркурий': send_message_about_the_incorrect_choice(call, markup_question_6)
            
            elif call.data == 'Сатурн': send_message_about_the_incorrect_choice(call, markup_question_6)


            elif call.data == 'Луна':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_8')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nЛуна — единственный естественный спутник Земли. Самый близкий к Солнцу спутник планеты, так как у ближайших к Солнцу планет (Меркурия и Венеры) их нет. Второй по яркости объект на земном небосводе после Солнца и пятый по величине естественный спутник планеты Солнечной системы. Среднее расстояние между центрами Земли и Луны — 384 467 км ( ~30 диаметров Земли).\n\nЛуна появилась около 4,5 млрд лет назад, немного позже Земли. Наиболее популярна гипотеза о том, что Луна сформировалась из осколков, оставшихся после «Гигантского столкновения» Земли и Тейи — планеты, схожей по размерам с Марсом.\nНа сегодняшний день Луна является единственным внеземным астрономическим объектом, на котором побывал человек.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Луна', reply_markup = markup)
            
            elif call.data == 'Комета Галлея': send_message_about_the_incorrect_choice(call, markup_question_7)
            
            elif call.data == 'Солнце(7)': send_message_about_the_incorrect_choice(call, markup_question_7)
            

            elif call.data == 'Лайка':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_9')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nЛайка (1954 — 3 ноября 1957) — собака-космонавт, первое животное, выведенное на орбиту Земли. Была запущена в космос 3 ноября 1957 года в половине шестого утра по московскому времени на советском корабле «Спутник-2». На тот момент Лайке было около трёх лет. Возвращение Лайки на Землю конструкцией космического аппарата не предусматривалось. Собака погибла во время полёта через 5—7 часов после старта от перегрева, хотя предполагалось, что она проживёт на орбите около недели\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Лайка_(собака-космонавт)', reply_markup = markup)
            
            elif call.data == 'Белка': send_message_about_the_incorrect_choice(call, markup_question_8)
            
            elif call.data == 'Стрелка': send_message_about_the_incorrect_choice(call, markup_question_8)


            elif call.data == '108 минут':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_10')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\n«Восток-1» («Восток») — советский космический корабль из серии «Восток», первый в мире космический аппарат, поднявший на своём борту человека на околоземную орбиту. На корабле «Восток» 12 апреля 1961 года лётчик-космонавт СССР Юрий Алексеевич Гагарин совершил первый в мире пилотируемый полёт в космическое пространство. Старт корабля состоялся с советского космодрома «Байконур» в 9 часов 7 минут по московскому времени (06:07:00 UTC). Корабль выполнил один оборот вокруг Земли и совершил посадку в 10 часов 53 минут (07:55:00 UTC) в районе деревни Смеловка Саратовской области. Длительность полёта составила 108 минут.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Восток-1', reply_markup = markup)
            
            elif call.data == '45 минут': send_message_about_the_incorrect_choice(call, markup_question_9)
            
            elif call.data == '20 минут': send_message_about_the_incorrect_choice(call, markup_question_9)


            elif call.data == 'Герман Титов':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_11')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nГерман Степанович Титов (11 сентября 1935, Верх-Жилино — 20 сентября 2000, Москва) — советский космонавт, первый человек, совершивший длительный космический полёт (более суток), второй советский космонавт, второй человек в мире, совершивший орбитальный космический полёт. Самый молодой человек в истории, совершивший орбитальный космический полёт. Герой Советского Союза (9 августа 1961 года). Дублёр Юрия Гагарина; доктор военных наук.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Титов,_Герман_Степанович', reply_markup = markup)
            
            elif call.data == 'Валерий Быковский': send_message_about_the_incorrect_choice(call, markup_question_10)
            
            elif call.data == 'Андриян Николаев': send_message_about_the_incorrect_choice(call, markup_question_10)


            elif call.data == 'Восток':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_12')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\n«Восток-1» («Восток») — советский космический корабль из серии «Восток», первый в мире космический аппарат, поднявший на своём борту человека на околоземную орбиту. На корабле «Восток» 12 апреля 1961 года лётчик-космонавт СССР Юрий Алексеевич Гагарин совершил первый в мире пилотируемый полёт в космическое пространство. Старт корабля состоялся с советского космодрома «Байконур» в 9 часов 7 минут по московскому времени (06:07:00 UTC). Корабль выполнил один оборот вокруг Земли и совершил посадку в 10 часов 53 минут (07:55:00 UTC) в районе деревни Смеловка Саратовской области. Длительность полёта составила 108 минут.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Восток-1', reply_markup = markup)
            
            elif call.data == 'Союз': send_message_about_the_incorrect_choice(call, markup_question_9)
            
            elif call.data == 'Восход': send_message_about_the_incorrect_choice(call, markup_question_9)


            elif call.data == 'Кедр':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_13')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\n12 апреля 1961 года был совершён первый полёт человека в космос. Этим "счастливчиком" стал Юрий Алексеевич Гагарин(9.03.1934 - 27.03.1968). Ракета-носитель «Восток» с кораблём «Восток-1», на борту которого находился Гагарин, была запущена с космодрома Байконур, расположенного в Кызылординской области Казахской ССР. После 108 минут[5] полёта Гагарин успешно приземлился в Саратовской области, неподалёку от Энгельса.\n\n12 апреля 1961 года, день полёта Юрия Гагарина в космос, был объявлен праздником — Днём космонавтики. В честь первого космонавта Земли был переименован ряд населённых пунктов (включая его родной город — Гжатск), названы улицы и проспекты. В разных городах мира было установлено множество памятников Гагарину.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Гагарин,_Юрий_Алексеевич', reply_markup = markup)

            elif call.data == 'Земля': send_message_about_the_incorrect_choice(call, markup_question_12)
            
            elif call.data == 'Клен': send_message_about_the_incorrect_choice(call, markup_question_12)


            elif call.data == 'Алексей Леонов':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_14')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nАлексей Архипович Леонов (30 мая 1934 — 11 октября 2019) — лётчик-космонавт СССР № 11, первый человек в мире, вышедший в открытый космос. Дважды Герой Советского Союза (1965, 1975), генерал-майор авиации (1975), лауреат Государственной премии СССР (1981), член Высшего совета партии «Единая Россия» (2002—2019).\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Леонов,_Алексей_Архипович', reply_markup = markup)

            elif call.data == 'Джон Янг': send_message_about_the_incorrect_choice(call, markup_question_13)
            
            elif call.data == 'Эдвард Уайт': send_message_about_the_incorrect_choice(call, markup_question_13)


            elif call.data == 'Светлана Савицкая':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_15')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nСветлана Евгеньевна Савицкая (8 августа 1948) — советский космонавт, лётчик-испытатель, педагог и общественный деятель, кандидат технических наук, майор военно-воздушных сил СССР. Вторая в мире женщина-космонавт после Валентины Терешковой. Первая в мире женщина-космонавт, вышедшая в открытый космос.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Савицкая,_Светлана_Евгеньевна', reply_markup = markup)

            elif call.data == 'Салли Райд': send_message_about_the_incorrect_choice(call, markup_question_14)
            
            elif call.data == 'Валентина Терешкова(14)': send_message_about_the_incorrect_choice(call, markup_question_14)


            elif call.data == 'Пионер':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_16')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\n«Пионер-11» (англ. Pioneer 11, Pioneer G) — космический зонд НАСА, предназначенный для изучения Юпитера и Сатурна. Первый космический аппарат, пролетевший в окрестностях Сатурна, и второй (после «Пионера-10»), пролетевший в окрестностях Юпитера.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Пионер-11', reply_markup = markup)

            elif call.data == 'Шаттл': send_message_about_the_incorrect_choice(call, markup_question_15)
            
            elif call.data == 'Викинг': send_message_about_the_incorrect_choice(call, markup_question_15)


            elif call.data == 'Валентина Терешкова(16)':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_17')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nВалентина Владимировна Терешкова (6 марта 1937) — лётчик-космонавт СССР, первая в мире женщина-космонавт (1963), Герой Советского Союза (1963), генерал-майор (1995). Полный кавалер ордена «За заслуги перед Отечеством». Депутат Верховного Совета СССР VII—XI созывов (1966—1989), член Президиума Верховного Совета СССР (1974—1989). Глава Комитета советских женщин (1968—1987) и Союза советских обществ дружбы и культурной связи с зарубежными странами (1987—1992).Российский политик, депутат Государственной думы Российской Федерации, член Высшего совета партии «Единая Россия». В марте 2020 года предложила поправку к Конституции РФ, которая позволила действующему президенту России Владимиру Путину ещё дважды претендовать на пост президента.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Терешкова,_Валентина_Владимировна', reply_markup = markup)

            elif call.data == 'Елена Кондакова': send_message_about_the_incorrect_choice(call, markup_question_16)
            
            elif call.data == 'Пономарева Валентина': send_message_about_the_incorrect_choice(call, markup_question_16)


            elif call.data == 'Икар':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_18')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nЧтобы спастись с острова Крит от раздражённого Миноса, мастер Дедал сделал для себя и сына крылья, скреплённые воском, и Дедал просил: «Не поднимайся слишком высоко; солнце растопит воск. Не лети слишком низко; морская вода попадёт на перья, и они намокнут». Но уже во время перелёта в Элладу Икар настолько увлёкся полётом, что забыл наставление отца и поднялся очень высоко, подлетев слишком близко к Солнцу. Лучи Солнца растопили воск, Икар упал и утонул недалеко от острова Самос в море, которое и получило в этой части название Икарийского. Его тело, прибитое волнами к берегу, было похоронено Гераклом на маленьком островке Долиха, названном в его честь Икария.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Икар', reply_markup = markup)

            elif call.data == 'Геракл': send_message_about_the_incorrect_choice(call, markup_question_17)
            
            elif call.data == 'Минотавр': send_message_about_the_incorrect_choice(call, markup_question_17)


            elif call.data == 'Солнце(18)':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_19')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nСолнце — одна из звёзд нашей Галактики (Млечный Путь) и единственная звезда Солнечной системы. Вокруг Солнца обращаются другие объекты этой системы: планеты и их спутники, карликовые планеты и их спутники, астероиды, метеороиды, кометы и космическая пыль.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Солнце', reply_markup = markup)

            elif call.data == 'Альдебаран': send_message_about_the_incorrect_choice(call, markup_question_18)
            
            elif call.data == 'Сириус': send_message_about_the_incorrect_choice(call, markup_question_18)


            elif call.data == 'Блуждающая':
                markup = types.InlineKeyboardMarkup(row_width = 1)
                button = types.InlineKeyboardButton('Следующий вопрос', callback_data = 'Question_20')
                markup.add(button)
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nПланета — небесное тело, вращающееся по орбите вокруг звезды или её остатков, достаточно массивное, чтобы стать округлым под действием собственной гравитации, но недостаточно массивное для начала термоядерной реакции, и сумевшее очистить окрестности своей орбиты от планетезималей. Планетами греки называли т. н. «блуждающие звёзды». Во многих ранних культурах планеты рассматривались как носители божественного начала или, по крайней мере, статуса божественных эмиссаров. По мере развития науки представления о планетах менялись в немалой степени и благодаря открытию новых объектов и обнаружению различий между ними.\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Планета', reply_markup = markup)

            elif call.data == 'Альдебаран': send_message_about_the_incorrect_choice(call, markup_question_19)
            
            elif call.data == 'Круглая': send_message_about_the_incorrect_choice(call, markup_question_19)


            elif call.data == 'Марс':
                
                bot.edit_message_text(chat_id = call.message.chat.id, message_id =  call.message.message_id, text = 'Это правильный ответ!\n\nМарс — четвёртая по удалённости от Солнца и седьмая по размеру планета Солнечной системы; масса планеты составляет 10,7 % массы Земли. Названа в честь Марса — древнеримского бога войны, соответствующего древнегреческому Аресу. Также Марс называют «красной планетой» из-за красноватого оттенка поверхности, придаваемого ей минералом маггемитом — γ-оксидом железа(III).\n\nСсылка на статью в Википедии: https://ru.wikipedia.org/wiki/Марс')

                sleep(5)

                bot.send_message(call.message.chat.id, 'Это всего лишь небольшая часть вопросов, связанных с бесконечным космосом, и чем больше мы находим ответов, тем больше возникает вопросов. \nА так как космос бесконечен, жизни не хватит ответить хотя бы на малую часть этих вопросов.\nПобольше Вам ответов и интересных Вам вопросов! Спасибо, что воспользовались продукцией нашего бренд "КодНик"!')

            elif call.data == 'Уран': send_message_about_the_incorrect_choice(call, markup_question_20)
            
            elif call.data == 'Сатурн': send_message_about_the_incorrect_choice(call, markup_question_20)
            
    except: bot.send_message(call.message.chat.id, 'Соединение с сервером разорвано. Чтобы продолжить, перезапустите, пожалуйста, бота, введя /start')

bot.polling(non_stop = True)