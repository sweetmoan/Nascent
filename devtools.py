import serial , time

cprt=input('Com port:')

def jumper():
    try:
        ser = serial.Serial(f'COM{cprt}',9600)
        print('COM{cprt} connected')
    except:
        print('hardware not found')
        input()

        
    print('started')
    while True:
        data = ser.read()
        if data:
            if data==b"l":
                pyautogui.hotkey('ctrl', 'win','right')
                print('window changed')
            else:
                pass

def serialtest():
    try:
        ser = serial.Serial(f'COM{cprt}', 9600)
        print('COM{prt} connected')
    except:
        print('hardware not found')
        input()
        exit()
        
    print('opt{q} to quit')
    while True:
        i = input("Enter Input: ").strip()
        
        if i == "q":
            print('quiting..')
            break
        
        ser.write(i.encode())
        time.sleep(0.5)
        print(ser.readline().decode('ascii'))
    ser.close()

print('''
opt[j] for jumper
[a] for serial test
''')
main=input('>> ')
if main == 'j':
    jumper()
elif main == 'a':
    serialtest()
else:
    print('invalid input')
    input()
