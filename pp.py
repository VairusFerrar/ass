from vosk import Model, KaldiRecognizer #pip install vosk распознавание речи
import os, json #системные функции и строковая залупа хз для чего
import pyaudio #pip install PyAudio хуй знает
import pyttsx3 #pip install pyttsx3 для озвучки речи милой тяночкой
import random
import random2
from datetime import datetime
import webbrowser
from pyowm import OWM
from pyowm.utils.config import get_default_config
import pyperclip
import cv2
#Функция для распознавание речи
#Переменная what(что?) принимает значение про проговаривает 
#типа такой speak("Вадим долбаеб") а она такая Вадим долбаеб
def speak(what):
     speak_engine = pyttsx3.init()
     #Ну установка голоса
     voices = speak_engine.getProperty('voices')
     #Вывод шо сказала тяночка
     print( what )
     #Принимает значение шо надо сказать
     speak_engine.say( what )
     #Сказать и ждать
     speak_engine.runAndWait()
     #Стоп пауза
     speak_engine.stop()
#Функция прощания 
def goodbay():
    sho = ['До свидания','Всего хорошего','Жду нашей встречи']
    ka = random2.choice(sho)
    speak(ka)
    exit(0)
def mem():
    sho = ['Мне коробочку сока, пожалуйста - Какой вам сок? - Любой… - Я годится? - Ну давайте ягодицу. Каких только названий не придумают эти рекламщики', 'Любой парень будет у ваших ног. Главное с первого удара попасть ему в челюсть. Ха Ха Ха', 'Есть люди, кто достает мобильник из кармана, чтоб посмотреть время, потом убирает его и вспоминает, что забыл время посмотреть', 'Надпись на калитке: "Стучите громче, глухая собака!"','Не буду навязываться, захочет напишет" подумали оба', 'В последнее время я стал намного ближе к природе. Совсем озверел']
    ka = random2.choice(sho)
    speak(ka)
    return listen
def time():
    now = datetime.now()
    speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    return listen
def kot():
    sho = ['Вашего кота зовут Манник, вы вроде мне про него рассказывали ./Он вообще такой дебил, что написать про это можно целую книгу . Живёт он с вами, просит вечно жрачку, на что конечно-же уходит много денег .', 'Могу сказать про него в переносном смысле - мужик который нихрена не делает и сидиит днями за телевизором . Чем-то похож на вас.','Серая мышь, которая бесит своим поведением','Довольно милая, но агрессивная зараза.']
    ka = random2.choice(sho)
    speak(ka)
    return listen
def dela():
    sho = ['Отлично, а у вас хозяин?', 'Так себе,Хозяин, я заждалась вас','Плохо, а у вас?','Классно!']
    ka = random2.choice(sho)
    speak(ka)
def temperature(pog):
    owm = OWM('8fdfb48649ee4eb956660d7bfc8d94f2')
    place = pog
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    #температура
    t = w.temperature("celsius")
    t1 = t['temp']
    t2 = t['feels_like']
    t3 = t['temp_max']
    t4 = t['temp_min']
    wi = w.wind()['speed']
    speak(f"В городе {place} температура {t1}°, ощущается как {t2}°,cкорость ветра, {wi} метра в секунду")
def notepad():
    speak("Открываю ваш блокнот")
    os.system('notepad')
def password_generation():
    global password
    password = ""
    dlina = random.randint(10,15)
    for x in range(dlina):
        symbol = random.randint(0,3)
        if symbol == 0:
            password = password + chr(random.randint(48,57))
        if symbol == 1:
            password = password + chr(random.randint(65,90))
        if symbol == 2:
            password = password + chr(random.randint(97,122))
        if symbol == 2:
            password = password + random.choice("+-/*!&$#?=@<>")
    speak("Ваш пароль")
    print(password)
    speak("Желаете сохранить пароль?")  
    return listen
def photo():
    # Включаем первую камеру
    cap = cv2.VideoCapture(0)
    # "Прогреваем" камеру, чтобы снимок не был тёмным
    for i in range(30):
        cap.read()
    # Делаем снимок    
    ret, frame = cap.read()
    #название файла
    now = datetime.now()
    filename = "image_" + str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)+".png"
    #путь в папку
    put = (r'photos/')
    # Записываем в файл
    cv2.imwrite(put+filename, frame)   
    # Отключаем камеру
    cap.release()
    os.system("cls")
    speak("Фото сделано и сохранено в папку фото")
    return listen
def roulette():
    sho = ['У нас мертвяк! Может быть на том свете тебе повезёт больше. Покойся с миром.','Вот это смельчак! Ты выжил после нажатия на курок! Больше так не рискуй. Подумай о маме и папе!','Вы выжили! Но постарайтесь не рисковать!','На этот раз тебе повезло, но будет ли так в следующий раз?','Удача на твоей стороне! А давай еще?','Задумайся, стоит ли попробовать еще, если ДА то зачем тебе это?',]
    ka = random2.choice(sho)
    speak("Вы зарядили 1 патрон и раскрутили барабан: " + ka)
    speak("Я вас слушаю")
    return listen
def coin():
    sho = ['Вы кинули монетку, выпал ОРЕЛ','Вы кинули монетку, выпала РЕШКА']
    ka = random2.choice(sho)
    speak(ka)
    return listen
#Залупа для чтения голоса с микрофона
def listen():
    #указываем путь к папке model а то прога не запустится и обязательно флаг r
    model = Model(r"D:\zxc\model")
    os.system("cls")
    speak("Добрый день")
    speak("Я вас слушаю")
    rec = KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            x=json.loads(rec.Result())
            #Вывод то что сказал обязательно писать после x ["text"]
            print(x["text"])
            #ну тут понятно если ты сказал "прощай" вызывается функция goodbay()
            if x["text"] == "прощай" or x["text"] == "пока" or x["text"] == "до свидания":
                goodbay()
            elif x["text"] == "расскажи анекдот" or x["text"] == "анекдот" or x["text"] == "хочу посмеяться":
                mem()
            if x["text"] == "сколько время" or x["text"] == "который час" or x["text"] == "время":
                time()
            if x["text"] == "расскажи про кота" or x["text"] == "что с моим котом":
                kot()
            if x["text"] == "как дела" or x["text"] == "как жизнь молодая" or x["text"] == "как поживаешь":
                dela()
            if "скажи" in x["text"]:
                x["text"] = x["text"].lstrip("скажи")
                x["text"] = x["text"].replace(" ","",1)
                speak(x["text"])
            if "поиск" in x["text"]:
                x["text"] = x["text"].lstrip("поиск")
                x["text"] = x["text"].replace(" ","",1)
                webbrowser.open_new_tab('https://yandex.ru/search/?text=' + x["text"])
            if "погода" in x["text"] or "температура" in x["text"]:
                x["text"] = x["text"].lstrip("погода")
                pog = x["text"].replace(" ","",1)
                temperature(pog)
            if "блокнот" in x["text"] or "черновик" in x["text"]:
                notepad()
            if x["text"] == "генерировать пароль" or x["text"] == "сделать пароль":
                password_generation()
            if x["text"] == "сохранить пароль" or x["text"] == "скопировать пароль":
                pyperclip.copy(password)
                speak("Пароль успешно сохранён")
            if x["text"] == "сделай фото" or x["text"] == "селфи":
                photo()
            if x["text"] == "монетка" or x["text"] == "сыграем" or x["text"] == "играть":
                coin()
            if x["text"] == "русская рулетка" or x["text"] == "рулетка" or x["text"] == "испытать удачу":
                roulette()
            if "видео" in x["text"]:
                x["text"] = x["text"].lstrip("видео")
                x["text"] = x["text"].replace(" ","",1)
                webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + x["text"])
                
                
        else:
            #print(rec.PartialResult())
            pass
#Начало программы - приветствие
#Бесконечный цикл что бы постоянно запускал функцию listen и начинал слушать
while True:
    listen()