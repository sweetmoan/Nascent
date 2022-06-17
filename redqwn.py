

import pyaudio
import speech_recognition as sr
import pyttsx3 
import os ,time ,calendar ,datetime ,requests

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
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        text = r.listen(source)          
    data = '' "
    try:
        data = r.recognize_google(text)
        print(data)
    except sr.UnknownValueError:
       print("the audio was incomprehensible")
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
    month_names = ['January','February','March','April','May','June','July','August','September','October','November','December'] 
    ordinalNumbers = ['1st','2nd','3rd' , '4th', '5th' , '6th', '7th' , '8th', '9th', '10th' , '11th' , '12th' , '13th' , '14th' , '15th' , '16th' , '17th' , '18th' , '19th' , '20th' , '21th' , '22th' , '23th' , '24th' , '25th' ,'26th','27th','28th','29th','30th','31st']    
    say('Today is '+ weekday +' '+ month_names[monthNum - 1]+' the ' + ordinalNumbers[dayNum -1]+'.')

                
WAKE='yo'
print('running')
while True:
    print(f'listening for wake word')
    text = recognize() 

    if WAKE in text:
        say('listening')
        text = recognize()      
        TIME = ["whats the time","what's the time","what time is it","what is the time","the time"]
        for phrase in TIME:
            if phrase in text:
                print('get time..')
                now = datetime.datetime.now()
                meridiem = ''
                if now.hour >=12:
                    meridiem = 'p.m'
                    hour = now.hour - 12
                else:
                    meridiem = 'a.m'
                    hour = now.hour     
                if now.minute < 10:
                    minute = '0'+str(now.minute)
                else:
                    minute = str(now.minute)    
                say('it is '+str(hour)+ ':'+ minute+ ' '+ meridiem+'.')
                
        DATE = ["what's the date","whats the date","what is the date","what date","the date"]
        for phrase in DATE:
            if phrase in text:
                getDate()

                            



