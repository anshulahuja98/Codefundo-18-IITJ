import RPi.GPIO as GPIO
import time
from flask import Flask, request
import vlc
import requests
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
URL = "disaster-chain.eastus.cloudapp.azure.com/post"

@app.route('/post', methods=["POST"])
def postJsonHandler():
    data = request.get_json()
    print(data['values'])
    mod_ax= abs(data['values'][0])
    mod_ay= abs(data['values'][1])
    mod_az= abs(data['values'][2])
    data1= {'Ax':data['values'][0],
            'Ay':data['values'][1],
            'Az':data['values'][2]}
    r= requests.post(url= URL,data= data1)
    print(r)
    if mod_ax>1.5 or mod_ay>1.5 or mod_az>1.5:
        print("Earthquake Detected")
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        player = vlc.MediaPlayer("/home/pi/CFD-18/raspberry-pi/siren.mp3")
        player.play()
        time.sleep(24)
    else:
        print("You are safe")
    return ''
@app.route('/get', methods=["GET"])
def get():
    return 'GET'

app.run(host='0.0.0.0', port=8090, debug=True)
