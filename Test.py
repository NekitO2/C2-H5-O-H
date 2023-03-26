import telebot
from telebot import types

bot = telebot.TeleBot('5891506134:AAHYfMnjRB6hAvuAOvQJYv_J7BEO1ytcKY8')

@bot.message_handler(commands=['start'])

def send_start_message(message):


    markup = types.InlineKeyboardMarkup(row_width = 1)
    button1 = types.InlineKeyboardButton(text = 'Турция', callback_data = 'Турция')
    button2 = types.InlineKeyboardButton(text = 'Египет', callback_data = 'Египет')
    button3 = types.InlineKeyboardButton(text = 'Россия', callback_data = 'Россия')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выберите страну для путешествия', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'Турция')

def send_turkey(callback):

    markup = types.InlineKeyboardMarkup(row_width = 3)
    button1 = types.InlineKeyboardButton(text = 'Анталья', callback_data = 'Анталья')
    button2 = types.InlineKeyboardButton(text = 'Стамбул', callback_data = 'Стамбул')
    markup.add(button1, button2)

    bot.send_message(callback.message.chat.id, 'Какой город вас интересует', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'Египет')

def send_egipet(callback):

    markup = types.InlineKeyboardMarkup(row_width = 3)
    button1 = types.InlineKeyboardButton(text = 'Каир', callback_data = 'Каир')
    button2 = types.InlineKeyboardButton(text = 'Александрия', callback_data = 'Александрия')
    markup.add(button1, button2)
    bot.send_message(callback.message.chat.id, 'Выберите город', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'Россия')

def send_russia(callback):

    markup = types.InlineKeyboardMarkup(row_width = 3)
    button1 = types.InlineKeyboardButton(text = 'Сочи', callback_data = 'Сочи')
    button2 = types.InlineKeyboardButton(text = 'Москва', callback_data = 'Москва')
    markup.add(button1, button2)
    bot.send_message(callback.message.chat.id, 'Выберите город', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'Стамбул')

def send_stambul(callback):

    markup = types.InlineKeyboardMarkup(row_width = 3)
    button1 = types.InlineKeyboardButton(text = 'Флорента', callback_data = 'Флорента')
    button2 = types.InlineKeyboardButton(text = 'Пера Пэлэйс', callback_data = 'Пера Пэлэйс')
    markup.add(button1, button2)
    bot.send_message(callback.message.chat.id, 'Выберите отель', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'Анталья')

def send_antalia(callback):

    markup = types.InlineKeyboardMarkup(row_width = 3)
    button1 = types.InlineKeyboardButton(text = 'Адонис', callback_data = 'Адонис')
    button2 = types.InlineKeyboardButton(text = 'Фалкон', callback_data = 'Фалкон')
    markup.add(button1, button2)
    bot.send_message(callback.message.chat.id, 'Выберите отель', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'Каир')

def send_kair(callback):

    markup = types.InlineKeyboardMarkup(row_width = 3)
    button1 = types.InlineKeyboardButton(text = 'Абдин Пэлэйс', callback_data = 'Абдин Пэлэйс')
    button2 = types.InlineKeyboardButton(text = 'Амин', callback_data = 'Амин')
    markup.add(button1, button2)
    bot.send_message(callback.message.chat.id, 'Выберите отель', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'Александрия')

def send_alexandria(callback):

    markup = types.InlineKeyboardMarkup(row_width = 3)
    button1 = types.InlineKeyboardButton(text = 'Плаза', callback_data = 'Плаза')
    button2 = types.InlineKeyboardButton(text = 'Хэлман', callback_data = 'Хэлман')
    markup.add(button1, button2)
    bot.send_message(callback.message.chat.id, 'Выберите отель', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'Сочи')

def send_sochi(callback):

    markup = types.InlineKeyboardMarkup(row_width = 3)
    button1 = types.InlineKeyboardButton(text = 'Арфа', callback_data = 'Арфа')
    button2 = types.InlineKeyboardButton(text = 'Лес', callback_data = 'Лес')
    markup.add(button1, button2)
    bot.send_message(callback.message.chat.id, 'Выберите отель', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'Москва')

def send_moscow(callback):

    markup = types.InlineKeyboardMarkup(row_width = 3)
    button1 = types.InlineKeyboardButton(text = 'Националь', callback_data = 'Националь')
    button2 = types.InlineKeyboardButton(text = 'Хилтон', callback_data = 'Хилтон')
    markup.add(button1, button2)
    bot.send_message(callback.message.chat.id, 'Выберите отель', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'Адонис')

def send_adonis(callback):
 
    bot.send_message(callback.message.chat.id, '''В конце веселого и спокойного дня вы можете уютно погрузиться в сон в наших номерах с необыкновенной панорамой Средиземного моря и гор Торос.

                                                    Отель Adonis благодаря прекрасной морской панораме, бесподобному расположению и разнообразию номеров, соответствующих высоким стандартам качетсва, предлагает отпуск, который создаст впечатление уютного дома.\n\n\n\nhttps://www.adonishotel.com/''')

@bot.callback_query_handler(func = lambda callback: callback.data == 'Фалкон')

def send_falkon(callback):
    bot.send_message(callback.message.chat.id, '''Отель Falcon расположен в центре Антальи. На территории обустроен частный пляж с платформой, бассейны и лужайка в саду с видом на Средиземное море. К услугам гостей традиционная турецкая баня, сауна и теннисный корт.

                                                Во всех номерах постелен паркетный пол и имеется балкон с видом на море и окрестности. В число удобств входит кондиционер, мини-бар и спутниковое телевидение. Собственная ванная комната укомплектована феном.

                                                В главном ресторане отеля Falcon предлагаются блюда турецкой и интернациональной кухни, которые сервируются в формате «шведского стола» в помещении и на открытом воздухе. В ресторане и во всех барах представлен ассортимент напитков.

                                                Гости могут посетить фитнес-центр и заказать расслабляющий массаж. На территории отеля оборудован теннисный корт и открытый бассейн с водными горками. В местах общего пользования предоставляется бесплатный Wi-Fi.

                                                Отель находится всего в 5 км от старинного района Калеичи — старого города Антальи и в 17 км от международного аэропорта Анталья. Стойка регистрации открыта круглосуточно. Гости могут воспользоваться камерой хранения багажа.\n\n\n\nhttps://www.booking.com/hotel/tr/club-falcon.ru.html''')


@bot.callback_query_handler(func = lambda callback: callback.data == 'Флорента')

def send_florenta(callback):
    bot.send_message(callback.message.chat.id, '''Отель Florenta расположен в центре Старого города, в 600 метрах от собора Святой Софии и дворца Топкапы. К услугам гостей номера с кондиционером, бесплатным Wi-Fi, телевизором с плоским экраном и мини-баром.

                                                Все номера отеля Florenta обставлены современной мебелью. Собственная ванная комната укомплектована феном. Из некоторых номеров можно выйти на французский балкон.

                                                На террасе или в крытом лаундже для гостей сервируют завтрак «шведский стол». В баре на террасе подают прохладительные напитки. Кроме того, гости могут заказать блюда местной кухни в близлежащих ресторанах.\n\n\n\nhttps://www.booking.com/hotel/tr/florenta-hotel-istanbul.ru.html?aid=356980&label=gog235jc-1FCAMo5AE49gJIIVgDaMIBiAEBmAEhuAEXyAEM2AEB6AEB-AECiAIBqAIDuAL2g9ygBsACAdICJGI0MDY1ZDg0LTliZDMtNGNmYi05NzdjLWZlNDg1YzYxY2MzM9gCBeACAQ&sid=868c31d61b326123312f441edafac0d7&dest_id=-755070;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1679229734;srpvid=a8c559526df10584;type=total;ucfs=1&#hotelTmpl''')

@bot.callback_query_handler(func = lambda callback: callback.data == 'Пера Пэлэйс')

def send_pera_palace(callback):

    bot.send_message(callback.message.chat.id, '''Отель-музей особой категории Pera Palace, построенный в 1892 году архитектором франко-турецкого происхождения Александром Валлаури, оформлен в неоклассическом и восточном стилях, которые гармонично сочетаются с дизайном в стиле ар-нуво. Из роскошных номеров открывается великолепный вид на залив Золотой Рог и исторический район Пера Стамбула. К услугам гостей крытый бассейн. Поездка на метро до популярных торговых центров Cevahir, Kanyon и Zorlu занимает всего 20 минут.

                                                В классических номерах и люксах использованы европейские и османские элементы декора. Все номера располагают деревянным полом, французскими окнами, телевизором и мини-баром. Ванные комнаты отделаны мрамором в стиле традиционного хаммама. В большинстве номеров и люксов имеется балкон с видом на исторический район Пера и залив Золотой Рог.

                                                В ресторане Agatha, названном в честь знаменитого автора детективов Агаты Кристи, подают блюда современной турецкой кухни. Бар с террасой Orient пользуется популярностью среди представителей высшего света Стамбула и путешественников из многих стран мира. Кроме того, гости могут посетить чайный лаундж Kubbeli Saloon с неповторимой атмосферой и живой фортепианной музыкой.

                                                В классической французской кондитерской Patisserie de Pera можно заказать превосходные турецкие и французские сладости ручной работы, в том числе пирожные, печенье макарон, торты и домашний шоколад.

                                                В спа-центре Pera by Spa Soul к услугам гостей хаммам с пенистой ванной и классической мраморной полкой с подогревом, паровая баня, гидромассажная ванна, сауна и полностью оборудованный тренажерный зал. Крытый бассейн с функцией гидромассажа работает в летний и зимний сезон.\n\n\n\nhttps://www.booking.com/hotel/tr/pera-palace.ru.html?aid=356980&label=gog235jc-1FCAMo5AE49gJIIVgDaMIBiAEBmAEhuAEXyAEM2AEB6AEB-AECiAIBqAIDuAL2g9ygBsACAdICJGI0MDY1ZDg0LTliZDMtNGNmYi05NzdjLWZlNDg1YzYxY2MzM9gCBeACAQ&sid=868c31d61b326123312f441edafac0d7&dest_id=-755070;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1679229885;srpvid=fc7a599ec943020c;type=total;ucfs=1&#hotelTmpl''')

@bot.callback_query_handler(func = lambda callback: callback.data == 'Абдин Пэлэйс')

def send_abdeen_palace(callback):

    bot.send_message(callback.message.chat.id, '''Хостел Abdeen Palace расположен в Каире, в 1,1 км от площади Тахрир. К услугам гостей номера с кондиционером и общий лаундж. К услугам гостей семейные номера и терраса. В хостеле работает круглосуточная стойка регистрации, производится доставка еды и напитков в номер и предоставляются услуги обмена валюты.

                                                Все номера хостела оснащены телевизором с плоским экраном и спутниковыми каналами. Номера оснащены холодильником.

                                                Ежедневно в хостеле Abdeen Palace сервируется континентальный завтрак.

                                                Рынок Хан аль-Халили находится в 2 км от хостела, а Египетский музей — в 2,4 км. Расстояние от хостела Abdeen Palace до международного аэропорта Каира составляет 16 км.\n\n\n\nhttps://www.booking.com/hotel/eg/abdeen-palace.ru.html?label=yan104jc-1DCAMoQzjbA0ghWANowgGIAQGYASG4ARfIAQzYAQPoAQH4AQKIAgGoAgO4AtaZ4qAGwAIB0gIkNjhjMWM1OGItMzc5OC00ZjdiLWE2YzYtMTAxMWRlZWYyOTk32AIE4AIB&sid=12697a80b953e23b5039567152c357da&aid=357027&ucfs=1&arphpl=1&dest_id=-290692&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=f9f8757fedc800df&srepoch=1679330560&from_sustainable_property_sr=1&from=searchresults#hotelTmpl''')

@bot.callback_query_handler(func = lambda callback: callback.data == 'Амин')

def send_amin(callback):

    bot.send_message(callback.message.chat.id, '''Отель Amin расположен в Каире, в 300 метрах от главного корпуса Американского университета. К услугам гостей общий лаундж, круглосуточная стойка регистрации и терраса для загара. В ресторане подают стейки, а также блюда местной и ближневосточной кухни.

                                                В каждом номере отеля Amin есть кондиционер, шкаф для одежды и собственная ванная комната. В числе удобств — телевизор с плоским экраном. Из некоторых номеров открывается вид на город.

                                                Ежедневно в отеле Amin подают континентальный завтрак. По четвергам в вечернее время сервируют бесплатный ужин «шведский стол».

                                                В 600 метрах от отеля находится Каирский музей. Расстояние до международного аэропорта Каира составляет 17 км.\n\n\n\nhttps://www.booking.com/hotel/eg/amin.ru.html?aid=357027&label=yan104jc-1FCAMoQzjbA0ghWANowgGIAQGYASG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AtaZ4qAGwAIB0gIkNjhjMWM1OGItMzc5OC00ZjdiLWE2YzYtMTAxMWRlZWYyOTk32AIF4AIB&sid=12697a80b953e23b5039567152c357da&dest_id=-290692;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=6;hpos=6;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1679330560;srpvid=f9f8757fedc800df;type=total;ucfs=1&#hotelTmpl''')


@bot.callback_query_handler(func = lambda callback: callback.data == 'Плаза')

def send_plaza(callback):

    bot.send_message(callback.message.chat.id, '''К услугам гостей отеля, расположенного на прогулочной улице вдоль моря в Александрии, предоставляются просторные номера, в которых можно пользоваться бесплатным Wi-Fi. Из некоторых номеров открывается вид на дворец Сафа или на пляж и причал Санстефано. Он находится рядом с торговым центром Elite San Stefano.

                                                Номера и люксы отеля Plaza Alexandria оборудованы кондиционером. В них также можно смотреть программы кабельного телевидения. Некоторые номера располагают балконом. Во всех номерах предоставляется мини-бар и роскошные туалетно-косметические принадлежности в ванной комнате.

                                                Ежедневно подаётся завтрак "шведский стол". Вечером гости могут отведать различные интернациональные и местные блюда. Также производится обслуживание номеров, включая доставку завтрака.

                                                На стойке регистрации можно приобрести газеты. Персонал круглосуточной стойки регистрации поможет воспользоваться услугами прачечной и химчистки.\n\n\n\nhttps://www.booking.com/hotel/eg/plaza.ru.html?aid=357027&label=yan104jc-1FCAMoQzjbA0ghWANowgGIAQGYASG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AtaZ4qAGwAIB0gIkNjhjMWM1OGItMzc5OC00ZjdiLWE2YzYtMTAxMWRlZWYyOTk32AIF4AIB&sid=12697a80b953e23b5039567152c357da&dest_id=-290263;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=10;hpos=10;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1679331380;srpvid=9d0077199eae0934;type=total;ucfs=1&#hotelTmpl''')

@bot.callback_query_handler(func = lambda callback: callback.data == 'Хэлман')

def send_helman(callback):

    bot.send_message(callback.message.chat.id, '''Отель Helnan Palestine расположен посреди пышного сада площадью 1,4 кв. км, из которого открывается вид на бухту в Средиземном море. К услугам гостей открытый бассейн и отдельная терраса для загара рядом с морем. В каждом номере предоставляется бесплатный доступ в интернет и имеется балкон с видом на море.

                                                    Все номера отеля Helnan Palestine отличаются просторной планировкой и обставлены роскошной мебелью. На полу постелено ковровое покрытие в восточном стиле. В числе удобств — принадлежности для приготовления горячих напитков и спутниковое телевидение. Из некоторых номеров открывается вид на исторический дворец Монтаза.

                                                    Гости могут полностью отрешиться от забот и просто наслаждаться солнцем. В жаркие дни будет приятно освежиться в бассейне.

                                                    В ресторанах и барах отеля Palestine представлен широкий выбор блюд и напитков, которые подают в помещении и на открытом воздухе. В стильном пабе Bodega вечером устраивают развлекательные мероприятия.

                                                    Отель Helnan находится в тихом, уединенном месте всего в 12 км от оживленного центра города Александрия и буквально в нескольких шагах от песчаного пляжа.\n\n\n\nhttps://www.booking.com/hotel/eg/helnan-palestine.ru.html?aid=357027&label=yan104jc-1FCAMoQzjbA0ghWANowgGIAQGYASG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AtaZ4qAGwAIB0gIkNjhjMWM1OGItMzc5OC00ZjdiLWE2YzYtMTAxMWRlZWYyOTk32AIF4AIB&sid=12697a80b953e23b5039567152c357da&dest_id=-290263;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=11;hpos=11;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1679331380;srpvid=9d0077199eae0934;type=total;ucfs=1&#hotelTmpl''')

@bot.callback_query_handler(func = lambda callback: callback.data == 'Арфа')

def send_arfa(callback):

    bot.send_message(callback.message.chat.id, '''Здесь созданы все условия для комфортного проживания — есть кондиционер, холодильник, телевизор, фен, утюг, чай/кофе в номерах, чайник, микроволновая печь, посудомойка, кухонная плита, сейф, отопление, терраса, мини-бар. В гостинице около 171 номеров — можно выбрать любой понравившийся и узнать подробнее, что в нём. По запросу предоставляются номера для некурящих. Уборка — каждый день.

                                                Берите своих питомцев — им будут рады!

                                                В гостинице есть ресторан, бар, тренажёрный зал, сауна, конференц-зал. Можно прогуляться по территории и в саду. И вы наверняка захотите отдохнуть у бассейна — он тут тоже есть. Причём крытый, открытый, сезонный. Море тут близко — до него всего 92 м, поэтому легко можно планировать пляжный отдых. Есть возможность взять напрокат машину, велосипед.

                                                У каждого гостя будет доступ в интернет, вы сможете выложить фотографии, отправить файл или позвонить родным по видео.

                                                Учитывайте время заселения в гостиницу. Заезд здесь начинается с 14:00, выехать нужно до 12:00. Даже если вы прибудете поздно ночью, вас встретят на круглосуточной стойке регистрации и помогут с размещением. Лифт внутри есть.

                                                Если вы на машине, можете оставить её на парковке. Если вы добираетесь своим ходом, воспользуйтесь услугой трансфера.

                                                За любой помощью обращайтесь на ресепшн. К вашим услугам: химчистка, прачечная, обслуживание номеров, консьерж-сервис, камера хранения.\n\n\n\nhttps://travel.yandex.ru/hotels/krasnodar-krai/arfa/?adults=2&checkinDate=2023-03-22&checkoutDate=2023-03-23&childrenAges=&searchPagePollingId=39f87a9214b28df624cb8700e219c82e-0-newsearch&seed=portal-hotels-search''')

@bot.callback_query_handler(func = lambda callback: callback.data == 'Лес')

def send_les(callback):

    bot.send_message(callback.message.chat.id, '''Здесь созданы все условия для комфортного проживания — есть кондиционер, холодильник, фен, утюг, чай/кофе в номерах, чайник, кофеварка, сейф, отопление, терраса, мини-бар. В гостинице около 24 номеров — можно выбрать любой понравившийся и узнать подробнее, что в нём. По запросу предоставляются номера для некурящих. Уборка — каждый день.

                                                Берите своих питомцев — им будут рады!

                                                В гостинице есть ресторан, бар, сауна. Можно прогуляться по территории и в саду. И вы наверняка захотите отдохнуть у бассейна — он тут тоже есть. Причём открытый, сезонный, с подогревом. Есть возможность взять напрокат велосипед.

                                                У каждого гостя будет доступ в интернет, вы сможете выложить фотографии, отправить файл или позвонить родным по видео.

                                                Учитывайте время заселения в гостиницу. Заезд здесь начинается с 14:00, выехать нужно до 12:00. Даже если вы прибудете поздно ночью, вас встретят на круглосуточной стойке регистрации и помогут с размещением.

                                                Если вы на машине, можете оставить её на парковке.

                                                За любой помощью обращайтесь на ресепшн. К вашим услугам: химчистка, прачечная, обслуживание номеров, камера хранения.\n\n\n\nhttps://travel.yandex.ru/hotels/sochi/les-glemping-i-spa/?adults=2&checkinDate=2023-03-22&checkoutDate=2023-03-23&childrenAges=&searchPagePollingId=39f87a9214b28df624cb8700e219c82e-0-newsearch&seed=portal-hotels-search''')

@bot.callback_query_handler(func = lambda callback: callback.data == 'Националь')

def send_national(callback):

    bot.send_message(callback.message.chat.id, '''Здесь созданы все условия для комфортного проживания — есть кондиционер, телевизор, фен, утюг, чай/кофе в номерах, чайник, сейф, отопление, мини-бар. В гостинице около 202 номеров — можно выбрать любой понравившийся и узнать подробнее, что в нём. По запросу предоставляются номера для некурящих. Уборка — каждый день.

                                                В гостинице есть ресторан, бар, тренажёрный зал, сауна, конференц-зал. И вы наверняка захотите отдохнуть у бассейна — он тут тоже есть. Причём крытый, с подогревом.

                                                У каждого гостя будет доступ в интернет, вы сможете выложить фотографии, отправить файл или позвонить родным по видео.

                                                Учитывайте время заселения в гостиницу. Заезд здесь начинается с 14:00, выехать нужно до 12:00. Даже если вы прибудете поздно ночью, вас встретят на круглосуточной стойке регистрации и помогут с размещением. Лифт внутри есть.

                                                Если вы на машине, можете оставить её на парковке.

                                                За любой помощью обращайтесь на ресепшн. К вашим услугам: химчистка, прачечная, обслуживание номеров, консьерж-сервис, камера хранения, ускоренная регистрация заезда/отъезда.\n\n\n\nhttps://travel.yandex.ru/hotels/moscow/natsional/?adults=2&checkinDate=2023-03-29&checkoutDate=2023-03-30&childrenAges=&searchPagePollingId=f4b24c39c8654dbae2e9785d6e93b144-0-newsearch&seed=portal-hotels-search''')

@bot.callback_query_handler(func = lambda callback: callback.data == 'Хилтон')

def send_hilton(callback):

    bot.send_message(callback.message.chat.id, '''Здесь созданы все условия для комфортного проживания — есть кондиционер, телевизор, фен, утюг, чай/кофе в номерах, сейф, отопление, мини-бар. В гостинице около 273 номеров — можно выбрать любой понравившийся и узнать подробнее, что в нём. По запросу предоставляются номера для некурящих. Уборка — каждый день.

                                                Берите своих питомцев — им будут рады!

                                                В гостинице есть ресторан, бар, тренажёрный зал, сауна, конференц-зал. И вы наверняка захотите отдохнуть у бассейна — он тут тоже есть. Причём крытый, с подогревом.

                                                У каждого гостя будет доступ в интернет, вы сможете выложить фотографии, отправить файл или позвонить родным по видео.

                                                Учитывайте время заселения в гостиницу. Заезд здесь начинается с 14:00, выехать нужно до 12:00. Даже если вы прибудете поздно ночью, вас встретят на круглосуточной стойке регистрации и помогут с размещением. Лифт внутри есть.

                                                Если вы добираетесь своим ходом, воспользуйтесь услугой трансфера.

                                                За любой помощью обращайтесь на ресепшн. К вашим услугам: химчистка, прачечная, обслуживание номеров, консьерж-сервис, камера хранения.\n\n\n\nhttps://travel.yandex.ru/hotels/moscow/khilton-moskva-leningradskaia/?adults=2&checkinDate=2023-03-29&checkoutDate=2023-03-30&childrenAges=&searchPagePollingId=f4b24c39c8654dbae2e9785d6e93b144-0-newsearch&seed=portal-hotels-search''')

bot.polling(non_stop = True)

