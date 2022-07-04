import subprocess
print('python 3.6 is needed')
input('press enter to proceed..')
print('installing requirements.. ')
try:
    subprocess.call(['pip','install','pyaudio'])
    subprocess.call(['pip','install','pyttsx3'])
    subprocess.call(['pip','install','SpeechRecognition'])
    subprocess.call(['pip','install','threaded'])
    subprocess.call(['pip','install','datetime'])
except:
    print('error')
    input('')
