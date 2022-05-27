import pyaudio
import speech_recognition as sr
import pyttsx3 
import os ,time ,calendar ,datetime ,requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',150)
engine.setProperty('voices', voices[1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()
    
  

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = int(kelvin - 273.15)
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit
    
def weather_status():
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
    API_KEY = 'bc27ac4b77ed162dafb95d08c57e79a8'
    CITY = 'Tagbilaran city'
      
        
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    description = response['weather'][0]['description']
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    gen_weather = 'weather reading in '+CITY+' is '+description
    celsius = 'temperature is '+str(temp_celsius)+' Celsius'
    wind = 'wind speed is '+str(wind_speed)
    humidity = 'humidity is '+str(humidity)

    print(gen_weather)
    print(celsius)
    print(wind+' m/s')
    print(humidity+'%\n')
    say(gen_weather)
    say(celsius)
    say(wind+ 'meter per second')
    say(humidity+'percent')



def audio_recognize():
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)          
    data = ''   
    try:
        data = r.recognize_google(audio)
        print('User said: '+data)
    except sr.UnknownValueError:
        pass
        #print("Couldn't understand the audio")
    except sr.RequestError as e:
        print(e) 
    
    return data
   

def getDate(): 
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day 
    month_names = ['January','February','March','April','May','June','July','August','September','October','November','December'] 
    ordinalNumbers = ['1st','2nd','3rd' , '4th', '5th' , '6th', '7th' , '8th', '9th', '10th' , '11th' , '12th' , '13th' , '14th' , '15th' , '16th' , '17th' , '18th' , '19th' , '20th' , '21th' , '22th' , '23th' , '24th' , '25th' ,'26th','27th','28th','29th','30th','31st']    
    return 'Today is '+ weekday +' '+ month_names[monthNum - 1]+' the ' + ordinalNumbers[dayNum -1]+'.'


	
while True:
    text = audio_recognize() 
    
    if('date' in text):
        print(getDate()),say(getDate())
    
    if('time' in text):
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
        print('It is '+str(hour)+ ':'+ minute+ ' '+ meridiem+'.')
        say('It is '+str(hour)+ ':'+ minute+ ' '+ meridiem+'.')

        
    if('exit' in text):
        say('as you wish')
        break
        
    if('weather' in text):
        weather_status()


