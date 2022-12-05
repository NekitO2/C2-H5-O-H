# This Python file uses the following encoding: utf-8
import os
import random
import threading
import time
import wave

import pyaudio

len_power = []
len_torque = []
len_weight = []
len_doors = []
len_type_of_body = [] 
len_fuel = [] 
len_engine_location = [] 
len_number_of_seats = [] 
len_drive = [] 
len_transfers = [] 

try_it_a_second_time = 0

class Car:
    def __init__(self, power, torque, weight, doors, type_of_body, fuel, engine_location, number_of_seats, drive, transfers):
        self.power = power
        self.torque = torque
        self.weight = weight 
        self.doors = doors
        self.type_of_body = type_of_body
        self.fuel = fuel
        self.engine_location = engine_location
        self.number_of_seats = number_of_seats
        self.drive = drive
        self.transfers = transfers

class Vehicle(Car):
    def __init__(self, power, torque, weight, doors, type_of_body, fuel, engine_location, number_of_seats, drive, transfers):
        super().__init__(power, torque, weight, doors, type_of_body, fuel, engine_location, number_of_seats, drive, transfers)

users_vehicle = Vehicle('74', '116', '1460', '4', 'Sedan/Седан', 'Gasoline/Бензин', 'Front/Переднее', '3', 'Back/Задний', '5')
# users_vehicle = Vehicle(str(input('Введите мощность ')), str(input('Введите крутяший момент ')), str(input('Введите массу ')), str(input('Введите количество дверей ')), str(input('Введите тип кузова ')), str(input('Введите тип топлива ')), str(input('Введите расположение двигателя ')), str(input('Введите количество сидений ')), str(input('Введите тип привода ')), str(input('Введите количество передач ')))

for x in users_vehicle.power:
    len_power.append(x)

for x in users_vehicle.torque:
    len_torque.append(x)

for x in users_vehicle.weight:
    len_weight.append(x)

for x in users_vehicle.doors:
    len_doors.append(x)

for x in users_vehicle.type_of_body:
    len_type_of_body.append(x)

for x in users_vehicle.fuel:
    len_fuel.append(x)

for x in users_vehicle.engine_location:
    len_engine_location.append(x)

for x in users_vehicle.number_of_seats:
    len_number_of_seats.append(x)

for x in users_vehicle.drive:
    len_drive.append(x)

for x in users_vehicle.transfers:
    len_transfers.append(x)

class main:

    def sound_simulated_load():
        CHUNK = 1024
        file_sound_simulated_loading = wave.open("error.wav", 'rb')
        stream_simulated_loading = pyaudio.PyAudio().open(format = pyaudio.PyAudio().get_format_from_width(file_sound_simulated_loading.getsampwidth()),
                        channels = file_sound_simulated_loading.getnchannels(),
                        rate = file_sound_simulated_loading.getframerate(),
                        output = True)
        data = file_sound_simulated_loading.readframes(CHUNK)
        while data != '':
            stream_simulated_loading.write(data)
            data = file_sound_simulated_loading.readframes(CHUNK)

    sound_simulated_loading_double_1 = threading.Thread(target = sound_simulated_load)
    sound_simulated_loading_double_2 = threading.Thread(target = sound_simulated_load)

    def sound_keyboard():
        CHUNK = 1024
        sound_keyboard = wave.open("Klaviatura.wav", 'rb')
        stream_keyboard = pyaudio.PyAudio().open(format = pyaudio.PyAudio().get_format_from_width(sound_keyboard.getsampwidth()),
                        channels = sound_keyboard.getnchannels(),
                        rate = sound_keyboard.getframerate(),
                        output = True)
        data = sound_keyboard.readframes(CHUNK)
        while data != '':
            stream_keyboard.write(data)
            data = sound_keyboard.readframes(CHUNK)

    sound_keyboard_time_1 = threading.Thread(target = sound_keyboard)
    sound_keyboard_time_2 = threading.Thread(target = sound_keyboard)


    def simulated_load():
        a = ['!','1','@','2',' ','№',';','%',':','?','*','(',')','_','-','+','=','#','$','%','^','&','q','Q','w','W','e','E','r','R','t','T','y','Y','u','U','i','I','o','O','p','P','[',']','{','}','a','A','s','S','d','D','f','F','g','G','h','G','h','H','j','J','k','K','l','L',"'",'|','z','Z','x','X','c','C','v','V','b','B','n','N','m','M','<','>',',','.','й','Й','ц','Ц','у','У','к','К','е','Е','н','Н','г','Г','ш','Ш','щ','Щ','з','З','х','Х','ъ','Ъ','ф','Ф','ы','Ы','в','В','а','А','п','П','р','Р','о','О','л','Л','д','Д','ж','Ж','э','Э','я','Я','ч','Ч','с','С','м','М','и','И','т','Т','ь','Ь','б','Б','ю','Ю']
        for x in range(70):
            da = [a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)],a[random.randint(0,149)]]
            print(''.join(da))
            time.sleep(0.1)
            os.system('cls')

    simulated_loading_double_1 = threading.Thread(target = simulated_load)
    simulated_loading_double_2 = threading.Thread(target = simulated_load)




            
    def table():
        print('---------------------------------------------------------------------------------------------------')
        print('|                                                |                                                |')
        print('|Power/Мощность                                  |',users_vehicle.power,' ' * (45 - len(len_power)),'|')
        print('|------------------------------------------------|------------------------------------------------|')
        print('|Torque/Крутяший момент                          |',users_vehicle.torque,' ' * (45 - len(len_torque)),'|')
        print('|------------------------------------------------|------------------------------------------------|')
        print('|Weight/Масса                                    |',users_vehicle.weight,' ' * (45 - len(len_weight)),'|')
        print('|------------------------------------------------|------------------------------------------------|')
        print('|Doors/Количество дверей                         |',users_vehicle.doors,' ' * (45 - len(len_doors)),'|')
        print('|------------------------------------------------|------------------------------------------------|')
        print('|Type of body/Тип кузова                         |',users_vehicle.type_of_body,' ' * (45 - len(len_type_of_body)),'|')
        print('|------------------------------------------------|------------------------------------------------|')
        print('|Fuel/Тип топлива                                |',users_vehicle.fuel,' ' * (45 - len(len_fuel)),'|')
        print('|------------------------------------------------|------------------------------------------------|')
        print('|Engine location/Расположение двигателя          |',users_vehicle.engine_location,' ' * (45 - len(len_engine_location)),'|')
        print('|------------------------------------------------|------------------------------------------------|')
        print('|Number of seats/Количество сидений              |',users_vehicle.number_of_seats,' ' * (45 - len(len_number_of_seats)),'|')
        print('|------------------------------------------------|------------------------------------------------|')
        print('|Drive/Тип привода                               |',users_vehicle.drive,' ' * (45 - len(len_drive)),'|')
        print('|------------------------------------------------|------------------------------------------------|')
        print('|Transfers/Количество передач                    |',users_vehicle.transfers,' ' * (45 - len(len_transfers)),'|')
        print('|                                                |                                                |')
        print('---------------------------------------------------------------------------------------------------')

 
    
    print_table = threading.Thread(target = table)


main.simulated_loading_double_1.start()
main.sound_simulated_loading_double_1.start()
time.sleep(9)
print('Sorry')
main.sound_keyboard_time_1.start()
time.sleep(1.5)

print('Take 2')
main.sound_keyboard_time_2.start()
time.sleep(1.5)  
            
print('Сontinue? (1 = continue, 2 = finish) ')

if int(input()) == 1:
    time.sleep(1)
    main.simulated_loading_double_2.start()
    main.sound_simulated_loading_double_2.start()
    time.sleep(9)
    main.print_table.start()




        