import serial , time , pyautogui
from colorama import Fore ,init , Style
init(autoreset=True)
colr_grn=Style.BRIGHT+Fore.GREEN
colr_red=Style.BRIGHT+Fore.RED


cprt=input('Com port:')

def jumper():
    try:
        ser = serial.Serial(f'COM{cprt}',9600)
        print(colr_grn+f'COM{cprt} connected')
    except:
        print(colr_red+'hardware not found')
        return

        
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
        ser = serial.Serial(f'COM{cprt}',9600)
        print(colr_grn+f'COM{prt} connected')
    except:
        print(colr_red+'hardware not found')
        
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
    
menu=True
while menu:
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
