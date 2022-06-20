import pyaudio#pipwin install pyaudio
import speech_recognition as sr #SpeechRecognition
import pyttsx3 
import os ,time ,calendar ,datetime ,requests#datetime,requests
from colorama import Fore ,init, Style
from threading import Thread

init(autoreset=True)
colr_grn=Style.BRIGHT+Fore.GREEN
#hour = int(datetime.datetime.now().hour)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',150)
engine.setProperty('voices', voices[0].id)

def say(text):
    engine.say(text)
    engine.runAndWait() 

def recognize():
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        text = r.listen(source)          
    data = ''
    try:
        data = r.recognize_google(text)
        print(data)
    except:
        pass
       #print("the audio was incomprehensible")
    #except Exception as e:
        #print("Exception: " + str(e))
        
    return data
    
"""    
def wish():
    print("started")
    speak('hello sir')
    
    if 1 <=hour <=11:
        speak('good morning')
    elif 12 <= hour <= 17:
        speak('good afternoon')
    else :
        speak("good evening");
"""  
    
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day 
    month_names = ['january','february','march','april','may','june','july','august','september','october','november','december'] 
    ordinalNumbers = ['1','2','3' , '4', '5' , '6', '7' , '8', '9', '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19' , '20' , '21' , '22' , '23' , '24' , '25' ,'26','27','28','29','30','31']    
    date='today is '+ weekday.lower() +' '+ month_names[monthNum - 1] +' '+ ordinalNumbers[dayNum -1]
    say(date),print(f'Yuri: {date}')
def getTime():
    now = datetime.datetime.now()
    meridiem = ''
    if now.hour >=12:
        meridiem = 'pm'
        hour = now.hour - 12
    else:
        meridiem = 'am'
        hour = now.hour     
    if now.minute < 10:
        minute = '0'+str(now.minute)
    else:
        minute = str(now.minute)    
    time='it is '+str(hour)+ ':'+ minute+ ' '+ meridiem
    say(time),print(f'Yuri {time}')
        
def listening():
    now = datetime.datetime.now()
    print(f'{now.hour}:{now.minute} listening')

print(f'{colr_grn}started')
wakeword='yuri'
while True:
    Thread(target = listening).start()
    text = recognize()
    TIME = [wakeword+" what time is it"," whats the time"," what's the time"]
    for phrase in TIME:
        if phrase in text:
            getTime()
                      
    DATE = [wakeword+" what's the date"," whats the date"," what is the date"]
    for phrase in DATE:
        if phrase in text:
            getDate()
            
    if wakeword+' activate safe mode' in text:
        say('initializing, the safe mode sequence')




