from random import choice
import telebot
from telebot import types

bot = telebot.TeleBot('5891506134:AAHYfMnjRB6hAvuAOvQJYv_J7BEO1ytcKY8')


@bot.message_handler(commands = ['start'])

def send_start_message(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    
    item1 = types.KeyboardButton('Фильм')
    item2 = types.KeyboardButton('Сериал')
    item3 = types.KeyboardButton('Пословица')
    item4 = types.KeyboardButton('Поговорка')
    item5 = types.KeyboardButton('Формулы физики')
    item6 = types.KeyboardButton('Химическая реакция')
    
    markup.add(item1, item2, item3, item4, item5, item6)

    press = bot.send_message(message.chat.id, 'Нажми на кнопку - получишь результат!', reply_markup = markup)
    bot.register_next_step_handler(press, waiting_to_input)

@bot.message_handler(content_types = ['text'])

def waiting_to_input(message):
    
    if message.text == 'Фильм':
        
        message = bot.send_message(message.chat.id, 'Введите число от 0 до 27')
        bot.register_next_step_handler(message, get_cinema)
    
    elif message.text == 'Сериал':
        
        message = bot.send_message(message.chat.id, 'Введите число от 0 до 5')
        bot.register_next_step_handler(message, get_serial)
    
    elif message.text == 'Пословица':
        
        message = bot.send_message(message.chat.id, 'Введите число от 0 до 44')
        bot.register_next_step_handler(message, get_poslovitsa)
    
    elif message.text == 'Поговорка':
        
        message = bot.send_message(message.chat.id, 'Введите число от 0 до 37')
        bot.register_next_step_handler(message, get_pogovorka)

    elif message.text == 'Формулы физики':

        message = bot.send_message(message.chat.id, 'Введите число от 0 до 97')
        bot.register_next_step_handler(message, get_formyla_fizika)

    elif message.text == 'Химическая реакция':

        message = bot.send_message(message.chat.id, 'Введите число от 0 до 99')
        bot.register_next_step_handler(message, get_himicheskaya_reakciya)

@bot.message_handler(content_types = ['text'])

def get_cinema(message):
    
    try:
        cinemas = ['Первому игорку приготвиться', 
                   'Асса', 
                   'Форсаж', 
                   'Назад в будущее', 
                   'Игла', 
                   'Путешествие к центру Земли', 
                   'Артек. Большое путешествие', 
                   'Трансформеры', 
                   'Аватар', 
                   'Кавказская пленница', 
                   'Операция "Ы", или новые приключения Шурика', 
                   'Ирония судьбы', 
                   'Михаил Васильевич меняет профессию',
                   'Человек Паук',
                   'Ford против Ferrari',
                   'Брат',
                   'Бриллиантовая рука',
                   'Терминатор',
                   'Джентельмены удачи',
                   'Пираты Карибского моря',
                   'Гладиатор',
                   'Гарри Поттер',
                   'Вселенная Marvel',
                   'Титаник',
                   'Железный человек',
                   '12 стульев',
                   "Д'Артаньян и три мушкетёра",
                   'Люди в чёрном',]
        
        message = bot.send_message(message.chat.id, f'{cinemas[int(message.text)]}\n\n\nНажми на кнопку - получишь результат! Снова!')

        bot.register_next_step_handler(message, waiting_to_input)

    except:
        
        bot.send_message(message.chat.id, 'Моя твоя не понимать!')

@bot.message_handler(content_types = ['text'])

def get_serial(message):
    
    try:

        serials = ['Пёс', 
                   'Улица разбитых фонарей', 
                   'След', 
                   'Великолепный век', 
                   'Бригада',
                   'Скорая помощь',]
        
        message = bot.send_message(message.chat.id, f'{serials[int(message.text)]}\n\n\nНажми на кнопку - получишь результат! Снова!')
        bot.register_next_step_handler(message, waiting_to_input)


    except:

        bot.send_message(message.chat.id, 'Моя твоя не понимать!')

@bot.message_handler(content_types = ['text'])

def get_poslovitsa(message):
    
    try:
    
        poslovitsa = ['Не плюй в колодец, пригодится воды напиться.',
        'Не делай неприятностей кому-либо, иначе в будущем сам можешь лишиться поддержки.',
        'Под лежачий камень и вода не течет.',
        'Без труда не выловишь и рыбку из пруда.',
        'Дело не сдвинется с места, если ничего не предпринимать.',
        'Был бы лес, соловьи прилетят.',
        'Не беречь поросли, не видать и дерева.',
        'Кто не сажал дерева, тому не лежать в тени.',
        'Ласточка весну начинает, соловей кончает.',
        'Не зима знобит, а весна.',
        'Соколу лес не диво, волку зима за обычай.',
        'Застает зимушка в летнем платьице.',
        'Узок путь зимою, а жидок - весною.',
        'Кто весной не пролежит, весь год будет сыт.',
        'Около речки колодца не копают.',
        'Зима весну пугает, да всё равно тает.',
        'Была бы водица, а сено зародится.',
        'Кто земле дает, тому земля втройне отдает.',
        'Дорогой товар из земли растет.',
        'Кто любит земле кланяться - без добычи не останется.',
        'Когда поднимается одна пылинка, в ней содержится вся земля, когда распускается один цветок, раскрывается целый мир.',
        'Если пахать плугом, земля станет лугом.',
        'В феврале зима с весной встретятся впервой.',
        'С берега море красиво, а с моря - берег красив.',
        'Сугробы снега на полях - урожай зерна в закромах.',
        'Зима спросит, что летом припасено.',
        'Зимой солнце сквозь слезы смеется.',
        'Мороз и железо рвет, и на лету птицу бьет.',
        'Много снега - много хлеба, много воды - много травы.',
        'Весна красна, да голодна, осень дождлива, да сыта.',
        'Весна да осень - на дню погод восемь.',
        'Весенний дождь растит, осенний гноит.',
        'Летняя неделя дороже зимней.',
        'Лето - припасиха, а зима - подбериха.',
        'Октябрь ни колеса ни полоза не любит.',
        'В октябре с солнцем распрощайся, ближе к печке подбирайся.',
        'Ноябрь - сентябрев внук, октябрев сын, зиме родной брат.',
        'Одно дерево еще не лес.',
        'Без корня и полынь не растет.',
        'Не все стриги, что растет.',
        'Не все греет, что светит: луна светла, да без тепла.',
        'Пчела хоть и жалит, да мед дает.',
        'Как месяц не свети, а все не солнышко.',
        'Возле леса жить - голодному не быть.',
        'Не зная броду, не суйся в воду.']
        message = bot.send_message(message.chat.id, f'{poslovitsa[int(message.text)]}\n\n\nНажми на кнопку - получишь результат! Снова!')

        bot.register_next_step_handler(message, waiting_to_input)


    except:
        bot.send_message(message.chat.id, 'Моя твоя не понимать!')

@bot.message_handler(content_types = ['text'])

def get_pogovorka(message):
    
    try:

        pogovorka = ['Декабрь - шапка зимы, июль - макушка лета.',
        'Новый год - к весне поворот.',
        'Январь - году начало, зиме середина.',
        'В феврале зима с весной встретятся впервой.',
        'С берега море красиво, а с моря - берег красив.',
        'Сугробы снега на полях - урожай зерна в закромах.',
        'Зима спросит, что летом припасено.',
        'Зимой волка бойся, а летом мухи.',
        'Зимой солнце сквозь слезы смеется.',
        'Мороз и железо рвет, и на лету птицу бьет.',
        'Много снега - много хлеба, много воды - много травы.',
        'Весна красна, да голодна: осень дождлива, да сыта.',
        'Красна весна цветами, осень - снопами.',
        'Весна да осень - на дню погод восемь.',
        'Весенний дождь растит, осенний гноит.',
        'Где в апреле река, там в июле лужица.',
        'Летняя неделя дороже зимней.',
        'Лето - припасиха, а зима - подбериха.',
        'Лето собирает, а зима подъедает.',
        'Осенью и воробей богат.',
        'Осенью скот жиреет, человек добреет.',
        'Сентябрь кафтан с плеч срывает, тулуп надевает.',
        'Октябрь ни колеса ни полоза не любит.',
        'В октябре с солнцем распрощайся, ближе к печке подбирайся.',
        'В ноябре зима с осенью борется.',
        'Ноябрь - сентябрев внук, октябрев сын, зиме родной брат.',
        'Одно дерево еще не лес.',
        'Под большим деревом и гриб вольготней живет.',
        'Без корня и полынь не растет.',
        'Не все стриги, что растет.',
        'Ветра в рукавицу не поймаешь.',
        'Не все греет, что светит: луна светла, да без тепла.',
        'Пчела хоть и жалит, да мед дает.',
        'Не всегда молния ударяет там, где она сверкает.',
        'Как месяц не свети, а все не солнышко.',
        'Возле леса жить - голодному не быть.',
        'Для муравья и роса - наводнение.',
        'Не зная броду, не суйся в воду.']
        
        message = bot.send_message(message.chat.id, f'{pogovorka[int(message.text)]}\n\n\nНажми на кнопку - получишь результат! Снова!')

        bot.register_next_step_handler(message, waiting_to_input)


    except:

        bot.send_message(message.chat.id, 'Моя твоя не понимать!')

@bot.message_handler(content_types = ['text'])

def get_formyla_fizika(message):
    
    try:
        
        formyla = ['Давление Р=F/S',
                    'Плотность ρ=m/V',
                    'Давление на глубине жидкости P=ρ∙g∙h',
                    'Сила тяжести Fт=mg',
                    'Архимедова сила Fa=ρж∙g∙Vт',
                    'Уравнение движения при равноускоренном движении X=X₀+υ₀∙t+(a∙t²)/2, S= (υ²-υ₀²) /2а, S= (υ+υ₀) ∙t /2',
                    'Уравнение скорости при равноускоренном движении υ=υ₀+a∙t',
                    'Ускорение a=(υ-υ₀)/t',
                    'Скорость при движении по окружности υ=2πR/Т',
                    'Центростремительное ускорение a=υ2/R',
                    'Связь периода с частотой ν=1/T=ω/2π',
                    'II закон Ньютона F=ma',
                    'Закон Гука Fy=-kx',
                    'Закон Всемирного тяготения F=G∙M∙m/R²',
                    'Вес тела, движущегося с ускорением а↑ Р=m(g+a)',
                    'Вес тела, движущегося с ускорением а↓ Р=m(g-a)',
                    'Сила трения Fтр=µN',
                    'Импульс тела p=mυ',
                    'Импульс силы Ft=∆p',
                    'Момент силы M=F∙ℓ',
                    'Потенциальная энергия тела, поднятого над землей Eп=mgh',
                    'Потенциальная энергия упруго деформированного тела Eп=kx²/2',
                    'Кинетическая энергия тела Ek=mυ²/2',
                    'Работа A=F∙S∙cosα',
                    'Мощность N=A/t=F∙υ',
                    'Коэффициент полезного действия η=Aп/Аз',
                    'Период колебаний математического маятника T=2π√ℓ/g',
                    'Период колебаний пружинного маятника T=2 π √m/k',
                    'Уравнение гармонических колебаний Х=Хmax∙cos ωt',
                    'Связь длины волны, ее скорости и периода λ= υТ',
                    'Количество вещества ν=N/ Na',
                    'Молярная масса М=m/ν',
                    'Cр. кин. энергия молекул одноатомного газа Ek=3/2∙kT',
                    'Основное уравнение МКТ P=nkT=1/3nm₀υ²',
                    'Закон Гей - Люссака (изобарный процесс) V/T =const',
                    'Закон Шарля (изохорный процесс) P/T =const',
                    'Относительная влажность φ=P/P₀∙100%',
                    'Внутр. энергия идеал. одноатомного газа U=3/2∙M/µ∙RT',
                    'Работа газа A=P∙ΔV',
                    'Закон Бойля - Мариотта (изотермический процесс) PV=const',
                    'Количество теплоты при нагревании Q=Cm(T2-T1)',
                    'Количество теплоты при плавлении Q=λm',
                    'Количество теплоты при парообразовании Q=Lm',
                    'Количество теплоты при сгорании топлива Q=qm',
                    'Уравнение состояния идеального газа PV=m/M∙RT',
                    'Первый закон термодинамики ΔU=A+Q',
                    'КПД тепловых двигателей η= (Q1 - Q2)/ Q1',
                    'КПД идеал. двигателей (цикл Карно) η= (Т1 - Т2)/ Т1',
                    'Закон Кулона F=k∙q1∙q2/R²',
                    'Напряженность электрического поля E=F/q',
                    'Напряженность эл. поля точечного заряда E=k∙q/R²',
                    'Поверхностная плотность зарядов σ = q/S',
                    'Напряженность эл. поля бесконечной плоскости E=σ/2ε0',
                    'Диэлектрическая проницаемость ε=E0/E',
                    'Потенциальная энергия взаимод. зарядов W= k∙q1q2/R',
                    'Потенциал φ=W/q',
                    'Потенциал точечного заряда φ=k∙q/R',
                    'Напряжение U=A/q',
                    'Для однородного электрического поля U=E∙d',
                    'Электроемкость C=q/U',
                    'Электроемкость плоского конденсатора C=S∙ε∙ε0/d',
                    'Энергия заряженного конденсатора W=qU/2=q²/2С=CU²/2',
                    'Сила тока I=q/t',
                    'Сопротивление проводника R=ρ∙ℓ/S',
                    'Закон Ома для участка цепи I=U/R',
                    'Законы послед. соединения I1=I2=I, U1+U2=U, R1+R2=R',
                    'Законы паралл. соед. U1=U2=U, I1+I2=I, 1/R1+1/R2=1/R',
                    'Мощность электрического тока P=I∙U',
                    'Закон Джоуля-Ленца Q=I²Rt',
                    'Закон Ома для полной цепи I=ε/(R+r)',
                    'Ток короткого замыкания (R=0) I=ε/r',
                    'Вектор магнитной индукции B=Fmax/ℓ∙I',
                    'Сила Ампера Fa=IBℓsin α',
                    'Сила Лоренца Fл=Bqυsin α',
                    'Магнитный поток Ф=BSсos α, Ф=LI',
                    'Закон электромагнитной индукции Ei=ΔФ/Δt',
                    'ЭДС индукции в движ проводнике Ei=Вℓυsinα',
                    'ЭДС самоиндукции Esi=-L∙ΔI/Δt',
                    'Энергия магнитного поля катушки Wм=LI²/2',
                    'Период колебаний кол. контура T=2π ∙√LC',
                    'Индуктивное сопротивление XL=ωL=2πLν',
                    'Емкостное сопротивление Xc=1/ωC',
                    'Действующее значение силы тока Iд=Imax/√2,',
                    'Действующее значение напряжения Uд=Umax/√2',
                    'Полное сопротивление Z=√(Xc-XL)²+R²',
                    'Закон преломления света n21=n2/n1= υ 1/ υ 2',
                    'Показатель преломления n21=sin α/sin γ',
                    'Формула тонкой линзы 1/F=1/d + 1/f',
                    'Оптическая сила линзы D=1/F',
                    'max интерференции: Δd=kλ,',
                    'min интерференции: Δd=(2k+1)λ/2',
                    'Диф.решетка d∙sin φ=k λ',
                    'Ф-ла Эйнштейна для фотоэффекта hν=Aвых+Ek, Ek=Uзе',
                    'Красная граница фотоэффекта νк = Aвых/h',
                    'Импульс фотона P=mc=h/ λ=Е/с',
                    'Закон радиоактивного распада N=N₀∙2-t/T',
                    'Энергия связи атомных ядер ECB=(Zmp+Nmn-Mя)∙c²',
                    'Постулаты теории относительности t=t1/√1-υ²/², ℓ=ℓ0∙√1-υ²/c², υ2=(υ1+υ)/1+ υ1∙υ/c², Е = mс²']
        
        message = bot.send_message(message.chat.id, f'{formyla[int(message.text)]}\n\n\nНажми на кнопку - получишь результат! Снова!')

        bot.register_next_step_handler(message, waiting_to_input)

    except:

        bot.send_message(message.chat.id, 'Моя твоя не понимать!')

@bot.message_handler(content_types = ['text'])

def get_himicheskaya_reakciya(message):

    reakciya = ['2KMnO4 + 3MnSO4 + 2H2O = 5MnO2 + K2SO4 + 2H2SO4',
                '2KMnO4 + 16HCl = 2MnCl2 + 5Cl2 + 8H2O + 2KCl',
                '5NaNO2 + 2KMnO4 + 3H2SO4 = 2MnSO4 + 5NaNO3 + K2SO4 + 3H2O',
                '10FeSO4 + 2KMnO4 + 8H2SO4 = 5Fe2(SO4)3 + 2MnSO4 + K2SO4 + 8H2O',
                '2KMnO4 + 5H2S + 3H2SO4 = 5S + 2MnSO4 + K2SO4 + 8H2O',
                '2KMnO4 + 5Na2SO3 + 3H2SO4 = MnSO4 + K2SO4 + 5Na2SO4 + 3H2O',
                'SO2 + 2KMnO4 + 4KOH = K2SO4 + 2K2MnO4 + 2H2O',
                'K2Cr2O7 + 3H2S + 4H2SO4 = Cr2(SO4)3 + 3S + K2SO4 + 7H2O',
                'K2Cr2O7 + 3NaNO2 + 4H2SO4 = 3NaNO3 + Cr2(SO4)3 + K2SO4 + 4H2O',
                'K2Cr2O7 + 6KI + 7H2SO4 = 3I2 + Cr2(SO4)3 + 4K2SO4 + 7H2O',
                '4Mg + 10HNO3(оч.разб.) = 4Mg(NO3)2 + NH4NO3 + 3H2O',
                'Cr2(SO4)3 + 3Br2 + 16NaOH = 6NaBr + 2Na2CrO4 + 3Na2SO4 + 8H2O',
                'Al2S3 + 30HNO3(конц.) = 2Al(NO3)3 + 3H2SO4 + 24NO2 + 12H2O',
                '6FeSO4 + 2HNO3 + 3H2SO4 = 3Fe2(SO4)3 + 2NO + 4H2O',
                'FeCl2 + 4HNO3(конц.) = Fe(NO3)3 + 2HCl + NO2 + H2O',
                'AlP + 11HNO3(конц.) = H3PO4 + 8NO2 + Al(NO3)3 + 4H2O',
                '6FeSO4 + KClO3 + 3H2SO4 = 3Fe2(SO4)3 + KCl + 3H2O',
                '3MnSO4 + 2KClO3 + 12KOH = 3K2MnO4 + 2KCl + 3K2SO4 + 6H2O',
                '2Al + K2Cr2O7 + 7H2SO4 = Al2(SO4)3 + Cr2(SO4)3 + K2SO4 + 7H2O',
                '3P2O3 + 2HClO3 + 9H2O = 6H3PO4 + 2HCl',
                'Cr2(SO4)3 + 6KMnO4 + 16KOH = 2K2CrO4 + 6K2MnO4 + 3K2SO4 + 8H2O',
                'Cr2O3 + 3KNO3 + 4KOH = 2K2CrO4 + 3KNO2 + 2H2O',
                '2NaNO2 + 2NaI + 2H2SO4 = 2NO + I2 + 2Na2SO4 + 2H2O',
                '8KI + 9H2SO4(конц.) = 4I2 + H2S + 8KHSO4 + 4H2O',
                'Cu + 2FeCl3 = CuCl2 + 2FeCl2',
                '3PH3 + 4HClO3 = 3H3PO4 + 4HCl',
                '3NO2 + H2O = NO + 2HNO3',
                'I2 + K2SO3 + 2KOH = 2KI + K2SO4 + H2O',
                '2NH3 + 3KClO = N2 + 3KCl + 3H2O',
                '6P + 5HClO3 + 9H2O = 5HCl + 6H3PO4',
                '3P + 5HNO3 + 2H2O = 3H3PO4 + 5NO',
                'Ca(ClO)2 + 4HCl = CaCl2 + 2Cl2 + 2H2O',
                '3H2S + HClO3 = 3S + HCl + 3H2O',
                'Fe2(SO4)3 + 2KI = 2FeSO4 + I2 + K2SO4',
                '2KMnO4 + KI + H2O = 2MnO2 + KIO3 + 2KOH',
                'I2 + 10HNO3(конц.) = 2HIO3 + 10NO2 + 4H2O',
                '3As2S3 + 28HNO3 + 4H2O = 6H3AsO4 + 28NO + 9H2SO4',
                '4Mg + 5H2SO4(конц.) = 4MgSO4 + H2S + 4H2O',
                'MnO2 + 2KBr + 2H2SO4 = MnSO4 + Br2 + K2SO4 + 2H2O',
                '5HCOH + 4KMnO4 + 6H2SO4 = 5CO2 + 2K2SO4 + 4MnSO4 + 11H2O',
                '3KNO2 + 2KMnO4 + H2O = 3KNO3 + 2MnO2 + 2KOH',
                'NaClO + 2KI + H2SO4 = I2 + NaCl + K2SO4 + H2O',
                '2KNO3 + 6KI + 4H2SO4 = 2NO + 3I2 + 4K2SO4 + 4H2O',
                '14HCl + K2Cr2O7 = 3Cl2 + 2CrCl3 + 2KCl + 7H2O',
                '2Cr(OH)3 + 3Cl2 + 10KOH = 2K2CrO4 + 6KCl + 8H2O',
                'K2MnO4 + 8HCl = MnCl2 + 2Cl2 + 2KCl + 4H2O',
                'K2Cr2O7 + 3Na2SO3 + 4H2O = 2Cr(OH)3 + 3Na2SO4 + 2KOH',
                '2KMnO4 + 10KBr + 8H2SO4 = 2MnSO4 + 5Br2 + 6K2SO4 + 8H2O',
                '4Zn + KNO3 + 7KOH = NH3 + 4K2ZnO2 + 2H2O',
                '2Fe(OH)3 + 3Br2 + 10KOH = 2K2FeO4 + 6KBr + 8H2O',
                'P2O3 + 6KOH + 2NO2 = 2NO + 2K3PO4 + 3H2O',
                '2KMnO4 + 2NH3 = 2MnO2 + N2 + 2KOH + 2H2O',
                '3Na2SO3 + 2KMnO4 + H2O = 3Na2SO4 + 2MnO2 + 2KOH',
                '3NaNO2 + Na2Cr2O7 + 8HNO3 = 5NaNO3 + 2Cr(NO3)3 + 4H2O',
                'B + HNO3(конц.) + 4HF = NO + HBF4 + 2H2O',
                '2CuCl2 + SO2 + 2H2O = 2CuCl + 2HCl + H2SO4',
                'PH3 + 8AgNO3 + 4H2O = 8Ag + H3PO4 + 8HNO3',
                '2NH3 + 6KMnO4 + 6KOH = N2 + 6K2MnO4 + 6H2O',
                '5Zn + 2KMnO4 + 8H2SO4 = 5ZnSO4 + 2MnSO4 + K2SO4 + 8H2O',
                '3KNO2 + K2Cr2O7 + 8HNO3 = 5KNO3 + 2Cr(NO3)3 + 4H2O',
                'FeS + 12HNO3(конц.) = Fe(NO3)3 + H2SO4 + 9NO2 + 5H2O',
                'KIO3 + 5KI + 3H2SO4 = 3I2 + 3K2SO4 + 3H2O',
                '2NaCrO2 + 3Br2 + 8NaOH = 2Na2CrO4 + 6NaBr + 4H2O',
                'Fe2(SO4)3 + Na2SO3 + H2O = 2FeSO4 + Na2SO4 + H2SO4',
                '3P2O3+ 2H2Cr2O7 + H2O = 2H3PO4 + 4CrPO4',
                '3Si + 4HNO3 + 18HF = 3H2SiF6 + 4NO + 8H2O',
                '5Na2SO3(нед.) + 2KIO3 + H2SO4 = I2 + K2SO4 + 5Na2SO4 + H2O',
                '2CrBr3 + 3H2O2 + 10NaOH = 2Na2CrO4 + 6NaBr + 8H2O',
                '8 KMnO4 + 5 PH3 + 12H2SO4 = 5H3PO4 + 8MnSO4 + 4K2SO4 + 12H2O',
                '3SO2 + K2Cr2O7 + H2SO4 = K2SO4 + Cr2(SO4)3 + H2O',
                '3P2O3 + 4HNO3 + 7H2O = 6H3PO4 + 4NO',
                '2NO + 3KClO + 2KOH = 2KNO3 + 3KCl + H2O',
                '5PH3 + 8KMnO4 + 12H2SO4 = 5H3PO4 + 4K2SO4 + 8MnSO4 + 12H2O',
                '5AsH3 + 8KMnO4 + 12H2SO4 = 5H3AsO4 + 4K2SO4 + 8MnSO4 + 12H2O',
                '2CuI + 4H2SO4(конц.) = 2CuSO4 + I2 + 4H2O + 2SO2',
                'Si + 2KOH + H2O = K2SiO3 + 2H2 (to)',
                'B + 3HNO3 = H3BO3 + 3NO2',
                '8NH3 + 3Br2 = N2 + 6NH4Br',
                'P4 + 3KOH + 3H2O = PH3 + 3KH2PO2',
                'Al2O3 + 3C + 3Cl2 = 2AlCl3 + 3CO(to)',
                'H2S + HClO = S + HCl + H2O',
                '5KNO3(расплав) + 2P = 5KNO2 + P2O5',
                'I2 + 5Cl2 + 6H2O = 2HIO3 + 10HCl',
                'H2S + 4Cl2 + 4H2O = H2SO4 + 8HCl',
                '8Zn + 5H2S2O7 = 8ZnSO4 + 2H2S + 3H2O',
                '2FeCl3 + 3Na2S = 2FeS + S + 6NaCl',
                'Na2S + 8NaNO3 + 9H2SO4 = 10NaHSO4 + 8NO2 + 4H2O',
                'Cr2O3 + 3NaNO3 + 2Na2CO3 = 2Na2CrO4 + 3NaNO2 + 2CO2',
                '5C + Ca3(PO4)2 + 3SiO2 = 2P + 5CO + 3CaSiO3 (to)',
                '2NaI + H2O2 + H2SO4 = Na2SO4 + I2 + 2H2O',
                '14HBr + K2Cr2O7 = 2CrBr3 + 3Br2 + 7H2O + 2KBr',
                '2NH3 + 2KMnO4(тв.) = N2 + 2MnO2 + 2KOH + 2H2O (to)',
                '2FeCl3 + SO2 + 2H2O = 2FeCl2 + H2SO4 + 2HCl',
                '2HMnO4 + 5H2S + 2H2SO4 = 5S + 2MnSO4 + 8H2O',
                '3KNO3 + 8Al + 5KOH + 18H2O = 3NH3 + 8K[Al(OH)4]',
                '5H2O2 + 2KMnO4 + 3H2SO4 = 5O2 + 2MnSO4 + K2SO4 + 8H2O',
                'P4 + 20HNO3 = 4H3PO4 + 20NO2 + 4H2O',
                '3NaClO + 4NaOH + Cr2O3 = 2Na2CrO4 + 3NaCl + 2H2O',
                'Na2SO3 + 2KMnO4 + 2KOH = 2K2MnO4 + Na2SO4 + H2O',
                'Cr2(SO4)3 + 3H2O2 + 10NaOH = 2Na2CrO4 + 3Na2SO4 +8H2O']
    
    message = bot.send_message(message.chat.id, f'{reakciya[int(message.text)]}\n\n\nНажми на кнопку - получишь результат! Снова!')

    bot.register_next_step_handler(message, waiting_to_input)


bot.polling(non_stop = True)