import telebot
from telebot import types

bot = telebot.TeleBot('5891506134:AAHYfMnjRB6hAvuAOvQJYv_J7BEO1ytcKY8')
markup_main = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton(text = 'Материнская плата', callback_data = 'Motherboard')
button2 = types.InlineKeyboardButton(text = 'Процессор', callback_data = 'CPU')
button3 = types.InlineKeyboardButton(text = 'Кулер', callback_data = 'FAN')
button4 = types.InlineKeyboardButton(text = 'Видеокарта', callback_data = 'GPU')
button5 = types.InlineKeyboardButton(text = 'Память', callback_data = 'RAM/ROM')
button6 = types.InlineKeyboardButton(text = 'Блок питания', callback_data = 'Power')
markup_main.add(button1, button2, button3, button4, button5, button6)

markup_cpu = types.InlineKeyboardMarkup(row_width = 4)
button1 = types.InlineKeyboardButton(text = 'Intel Core i3', callback_data = 'i3') 
button2 = types.InlineKeyboardButton(text = 'Intel Core i5', callback_data = 'i5') 
button3 = types.InlineKeyboardButton(text = 'Intel Core i7', callback_data = 'i7') 
button4 = types.InlineKeyboardButton(text = 'Intel Core i9', callback_data = 'i9') 
markup_cpu.add(button1, button2, button3, button4)

markup_motherboard = types.InlineKeyboardMarkup(row_width = 4)
button1 = types.InlineKeyboardButton(text = 'Asus', callback_data = 'Asus') 
button2 = types.InlineKeyboardButton(text = 'MSI', callback_data = 'MSI(motherboard)')
button3 = types.InlineKeyboardButton(text = 'Gigabyte', callback_data = 'Gigabyte(motherboard)')
button4 = types.InlineKeyboardButton(text = 'Asrock', callback_data = 'Asrock')
markup_motherboard.add(button1, button2, button3, button4)

markup_fan = types.InlineKeyboardMarkup(row_width = 4)
button1 = types.InlineKeyboardButton(text = 'ID-Cooling', callback_data = 'ID-Cooling')
button2 = types.InlineKeyboardButton(text = 'Zalman', callback_data = 'Zalman(fan)')
button3 = types.InlineKeyboardButton(text = 'DeepCool', callback_data = 'DeepCool')
button4 = types.InlineKeyboardButton(text = 'Cooler Master', callback_data = 'Cooler Master(fan)')
markup_fan.add(button1, button2, button3, button4)

markup_gpu = types.InlineKeyboardMarkup(row_width = 3)
button1 = types.InlineKeyboardButton(text = 'MSI', callback_data= 'MSI(gpu)') 
button2 = types.InlineKeyboardButton(text = 'Gigabyte', callback_data = 'Gigabyte(gpu)')
button3 = types.InlineKeyboardButton(text = 'Palit', callback_data = 'Palit')
markup_gpu.add(button1, button2, button3)

markup_ram_rom = types.InlineKeyboardMarkup(row_width = 2)
button1 = types.InlineKeyboardButton(text = 'Оперативная память', callback_data = 'RAM')
button2 = types.InlineKeyboardButton(text = 'HDD/SSD', callback_data = 'ROM')
markup_ram_rom.add(button1, button2)

markup_ram = types.InlineKeyboardMarkup(row_width = 3)
button1 = types.InlineKeyboardButton(text = 'Corsair', callback_data = 'Corsair')
button2 = types.InlineKeyboardButton(text = 'Kingston Fury', callback_data = 'Kingston Fury')
button3 = types.InlineKeyboardButton(text = 'Toshiba', callback_data = 'Toshiba')
markup_ram.add(button1, button2, button3)

markup_rom = types.InlineKeyboardMarkup(row_width = 2)
button1 = types.InlineKeyboardButton(text = 'HDD', callback_data = 'HDD')
button2 = types.InlineKeyboardButton(text = 'SSD', callback_data = 'SSD')
markup_rom.add(button1, button2)

markup_hdd = types.InlineKeyboardMarkup(row_width = 4)
button1 = types.InlineKeyboardButton(text = 'WD Gold', callback_data = 'WD Gold')
button2 = types.InlineKeyboardButton(text = 'WD Purple Pro', callback_data = 'WD Purple Pro')
button3 = types.InlineKeyboardButton(text = 'WD Red Pro', callback_data = 'WD Red Pro')
button4 = types.InlineKeyboardButton(text = 'Seagate', callback_data = 'Seagate')
markup_hdd.add(button1, button2, button3, button4)

markup_ssd = types.InlineKeyboardMarkup(row_width = 4)
button1 = types.InlineKeyboardButton(text = 'Intel', callback_data = 'Intel')
button2 = types.InlineKeyboardButton(text = 'WD Ultrastar', callback_data = 'WD Ultrastar')
button3 = types.InlineKeyboardButton(text = 'Kingston', callback_data = 'Kingston')
button4 = types.InlineKeyboardButton(text = 'Samsung', callback_data = 'Samsung')
markup_ssd.add(button1, button2, button3, button4)

markup_power = types.InlineKeyboardMarkup(row_width = 4)
button1 = types.InlineKeyboardButton(text = 'Cooler Master', callback_data = 'Cooler Master(power)')
button2 = types.InlineKeyboardButton(text = 'Thermaltake', callback_data = 'Thermaltake')
button3 = types.InlineKeyboardButton(text = 'Gigabyte', callback_data = 'Gigabyte(power)')
button4 = types.InlineKeyboardButton(text = 'Zalman', callback_data = 'Zalman(power)')
markup_power.add(button1, button2, button3, button4)

@bot.message_handler(commands=['start'])

def send_start_message(message):

    bot.send_message(message.chat.id, 'Выберите один из комплектующих ПК', reply_markup = markup_main)

@bot.callback_query_handler(func = lambda call: call.data == 'CPU')

def send_cpu(call):

    bot.send_message(call.message.chat.id, 'Выберите модель прoцессора', reply_markup = markup_cpu)

@bot.callback_query_handler(func = lambda call: call.data == 'Motherboard')

def send_motherboard(call):

    bot.send_message(call.message.chat.id, 'Выберите фирму производитель', reply_markup = markup_motherboard)

@bot.callback_query_handler(func = lambda call: call.data == 'FAN')

def send_fan(call):

    bot.send_message(call.message.chat.id, 'Выберите фирму произвоителя', reply_markup = markup_fan)

@bot.callback_query_handler(func = lambda call: call.data == 'GPU')

def send_gpu(call):

    bot.send_message(call.message.chat.id, 'Выберите фирму производитель', reply_markup = markup_gpu)

@bot.callback_query_handler(func = lambda call: call.data == 'RAM/ROM')

def send_ram_rom(call):

    bot.send_message(call.message.chat.id, 'Выберите тип памяти', reply_markup = markup_ram_rom)

@bot.callback_query_handler(func = lambda call: call.data == 'RAM')

def send_ram(call):

    bot.send_message(call.message.chat.id, 'Выберите фирму производитель', reply_markup = markup_ram)

@bot.callback_query_handler(func = lambda call: call.data == 'ROM')

def send_rom(call):

    bot.send_message(call.message.chat.id, 'Выберите тип памяти', reply_markup = markup_rom)

@bot.callback_query_handler(func = lambda call: call.data == 'HDD')

def send_hdd(call):

    bot.send_message(call.message.chat.id, 'Выберите фирму производителя', reply_markup = markup_hdd)

@bot.callback_query_handler(func = lambda call: call.data == 'SSD')

def send_ssd(call):

    bot.send_message(call.message.chat.id, 'Выберите фирму производителя', reply_markup = markup_ssd)

@bot.callback_query_handler(func = lambda call: call.data == 'Power')

def send_power(call):

    bot.send_message(call.message.chat.id, 'Выберите фирму производителя', reply_markup = markup_power)
















@bot.callback_query_handler(func = lambda call: call.data == 'i3')

def send_i3(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/processor-intel-s-core-i3-13100f-soc-1700-3-4ghz-oem-1901393/', reply_markup = markup_cpu)

@bot.callback_query_handler(func = lambda call: call.data == 'i5')

def send_i5(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/processor-intel-s-core-i5-13600kf-soc-1700-3-5ghz-oem-1872489/', reply_markup = markup_cpu)

@bot.callback_query_handler(func = lambda call: call.data == 'i7')

def send_i7(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/processor-intel-s-core-i7-13700kf-soc-1700-3-4ghz-oem-1873956/', reply_markup = markup_cpu)

@bot.callback_query_handler(func = lambda call: call.data == 'i9')

def send_i9(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/processor-intel-s-core-i9-13900kf-soc-1700-3-0ghz-oem-1881986/', reply_markup = markup_cpu)

@bot.callback_query_handler(func = lambda call: call.data == 'Asus')

def send_asus(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/materinskaya-plata-asus-rog-maximus-z690-formula-soc-1700-intel-z690-4-1646232/', reply_markup = markup_motherboard)

@bot.callback_query_handler(func = lambda call: call.data == 'MSI(motherboard)')

def send_msi_motherboard(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/materinskaya-plata-msi-mpg-z690-force-wifi-soc-1700-intel-z690-4xddr5-1845408/', reply_markup = markup_motherboard)

@bot.callback_query_handler(func = lambda call: call.data == 'Gigabyte(motherboard)')

def send_gigabyte(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/materinskaya-plata-gigabyte-z690-aorus-master-soc-1700-intel-z690-4xdd-1618777/', reply_markup = markup_motherboard)

@bot.callback_query_handler(func = lambda call: call.data == 'Asrock')

def send_asrock(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/materinskaya-plata-asrock-z790-pro-rs-wifi-soc-1700-intel-z790-4xddr5-1896155/', reply_markup = markup_motherboard)

@bot.callback_query_handler(func = lambda call: call.data == 'ID-Cooling')

def send_id_cooling(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/sistema-ohlazhdeniya-id-cooling-zoomflow-360-xt-soc-am4-1151-1200-2066-1622277/', reply_markup = markup_fan)

@bot.callback_query_handler(func = lambda call: call.data == 'Zalman(fan)')

def send_zalman_fan(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/ustroistvo-ohlazhdeniya-kuler-zalman-cnps20x-soc-fm2-am2-am3-am4-1150-1373161/', reply_markup = markup_fan)

@bot.callback_query_handler(func = lambda call: call.data == 'DeepCool')

def send_deepcool(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/sistema-vodyanogo-ohlazhdeniya-deepcool-le500-soc-am5-am4-1151-1200-17-1783514/', reply_markup = markup_fan)

@bot.callback_query_handler(func = lambda call: call.data == 'Cooler Master(fan)')

def send_cooler_master(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/ustroistvo-ohlazhdeniya-kuler-cooler-master-watercooler-ml120l-v2-rgb-1457484/', reply_markup = markup_fan)

@bot.callback_query_handler(func = lambda call: call.data == 'MSI(gpu)')

def send_msi_gpu(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/videokarta-msi-pci-e-4-0-rtx-4090-suprim-24g-nv-rtx4090-24576mb-384-gd-1896098/', reply_markup = markup_gpu)

@bot.callback_query_handler(func = lambda call: call.data == 'Gigabyte(gpu)')

def send_gigabyte_gpu(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/videokarta-gigabyte-pci-e-4-0-gv-n4090gaming-24gd-nv-rtx4090-24576mb-3-1893334/', reply_markup = markup_gpu)

@bot.callback_query_handler(func = lambda call: call.data == 'Palit')

def send_palit(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/videokarta-palit-pci-e-4-0-pa-rtx4090-gamerock-nv-rtx4090-24576mb-384-1859908/', reply_markup = markup_gpu)

@bot.callback_query_handler(func = lambda call: call.data == 'Corsair')

def send_corsair(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/pamyat-ddr4-32gb-5600mhz-corsair-cmt64gx5m2b5600c40-rtl-dimm-rtl-1909871/', reply_markup = markup_ram)

@bot.callback_query_handler(func = lambda call: call.data == 'Kingston Fury')

def send_kingston_fury(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/pamyat-ddr4-4x131072-3600mhz-kingston-kf436c18bbk4-128-fury-beast-blac-1914364/', reply_markup = markup_ram)

@bot.callback_query_handler(func = lambda call: call.data == 'Toshiba')

def send_toshiba(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/zhestkii-disk-toshiba-sata-iii-14tb-mg07aca14te-enterprise-capacity-72-1794294/', reply_markup = markup_ram)

@bot.callback_query_handler(func = lambda call: call.data == 'WD Gold')

def send_wd_gold(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/zhestkii-disk-wd-sata-iii-18tb-wd181kryz-gold-7200rpm-512mb-3-5-1862211/', reply_markup = markup_hdd)

@bot.callback_query_handler(func = lambda call: call.data == 'WD Purple Pro')

def send_wd_purple_pro(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/zhestkii-disk-wd-sata-iii-18tb-wd181purp-purple-pro-7200rpm-512mb-3-5-1744121/', reply_markup = markup_hdd)

@bot.callback_query_handler(func = lambda call: call.data == 'WD Red Pro')

def send_wd_red_pro(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/zhestkii-disk-wd-sata-iii-12tb-wd121kfbx-red-pro-7200rpm-256mb-3-5-1878706/', reply_markup = markup_hdd)

@bot.callback_query_handler(func = lambda call: call.data == 'Seagate')

def send_seagate(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/zhestkii-disk-seagate-sata-iii-16tb-st16000ne000-ironwolf-pro-7200rpm-1739583/', reply_markup = markup_hdd)

@bot.callback_query_handler(func = lambda call: call.data == 'Intel')

def send_intel(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/nakopitel-ssd-intel-s-pci-e-x4-7-5tb-ssdpe2ke076t801-dc-p4610-2-5-1725634/', reply_markup = markup_ssd)

@bot.callback_query_handler(func = lambda call: call.data == 'Ultrastar')

def send_ultrastar(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/nakopitel-ssd-wd-pci-e-3-1-6-25tb-0ts1878-wus4c6464dsp3x1-ultrastar-dc-1616802/', reply_markup = markup_ssd)

@bot.callback_query_handler(func = lambda call: call.data =='Kingston')

def send_kingston(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/nakopitel-ssd-kingston-pci-e-3-0-7-5tb-sedc1500m-7680g-dc1500m-2-5-1641746/', reply_markup = markup_ssd)

@bot.callback_query_handler(func = lambda call: call.data == 'Samsung')

def send_samsung(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/nakopitel-ssd-samsung-s-sata-iii-7-5tb-mz7l37t6hbla-00a07-pm893-2-5-1877890/', reply_markup = markup_ssd)

@bot.callback_query_handler(func = lambda call: call.data == 'Cooler Master(power)')

def send_cooler_master_power(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/blok-pitaniya-cooler-master-atx-2000w-m2000-80-platinum-24-8-4-4pin-ap-1847038/', reply_markup = markup_power)

@bot.callback_query_handler(func = lambda call: call.data == 'Thermaltake')

def send_thermaltake(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/blok-pitaniya-thermaltake-atx-1500w-toughpower-grand-tf1-80-titanium-2-1486287/', reply_markup = markup_power)

@bot.callback_query_handler(func = lambda call: call.data == 'Gigabyte(power)')

def send_gigabyte_power(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/blok-pitaniya-gigabyte-atx-1200w-gp-ap1200pm-80-platinum-24-4-4pin-apf-1624953/', reply_markup = markup_power)

@bot.callback_query_handler(func = lambda call: call.data == 'Zalman(power)')

def send_zalman(call):

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text ='https://www.citilink.ru/product/blok-pitaniya-zalman-atx-850w-zm850-arx-80-platinum-20-4pin-apfc-135mm-1774665/', reply_markup = markup_power)
    

bot.polling(non_stop = True)