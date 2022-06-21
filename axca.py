from flask import Flask, render_template, request

import serial, time#pyserial,flask 



app = Flask(_name_)



cport=input('Com Port:')



def serialcm:

  serialcomm = serial.Serial(cport,9600,timeout=1)



print('for web interface; [b] button or [i] input type.')

configure=input('[?]>')

if configure == 'b':

  index_page='''

  

  '''

elif configure =='a':

  index_page='''

  

  '''

else:

  print('invalid')

  time.sleep(1)

  print('closing..')

  time.sleep(2)

  exit()

  

@app.route("/", methods=['GET', 'POST'])

def index():

 

    if request.method == 'POST':

        

        if request.form.get('action1') == 'DAY':

            try:

                print('day')

                x='day'

                i=x.strip()

                serialcomm.write(i.encode())

            except:

                print('Serial error!')

        elif  request.form.get('action2') == 'NIGHT':

            try:

                print('night')

                x='night'

                i=x.strip()

                serialcomm.write(i.encode())

            except:

                print('Serial error!')           

        else:

            print('error')

    elif request.method == 'GET':

        return render_template('index.html')

    

    return render_template("index.html")





if _name_ == '_main_':

    app.run(debug=True,port=80)
Write to


