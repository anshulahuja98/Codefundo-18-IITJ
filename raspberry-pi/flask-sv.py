import RPi.GPIO as GPIO
import time
from flask import Flask, request
import vlc
import requests

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.HIGH)

URL = "http://disaster-chain.eastus.cloudapp.azure.com/post"
player = vlc.MediaPlayer("/home/pi/CFD-18/raspberry-pi/siren.mp3")


@app.route('/post', methods=["POST"])
def postJsonHandler():
    data = request.get_json()
    print(data['values'])
    mod_ax = abs(data['values'][0])
    mod_ay = abs(data['values'][1])
    mod_az = abs(data['values'][2])
    r = requests.post(url=URL, json=data)
    print(r)
    if mod_ax > 1.5 or mod_ay > 1.5 or mod_az > 1.5:
        print("Earthquake Detected")
        GPIO.output(31, 1)
        GPIO.output(33, 1)
        GPIO.output(37, 0)

        if not player.is_playing():
            player.play()
    else:
        print("You are safe")
    return ''


@app.route('/get', methods=["GET"])
def get():
    return 'GET'


app.run(host='0.0.0.0', port=8090, debug=True)
