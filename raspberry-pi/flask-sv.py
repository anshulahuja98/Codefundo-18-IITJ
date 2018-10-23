import RPi.GPIO as GPIO
import time
from flask import Flask, request
import vlc
#curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "userna$
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)

@app.route('/post', methods=["POST"])
def postJsonHandler():
    data = request.get_json()
    print(data['values'])
    mod_ax= abs(data['values'][0])
    mod_ay= abs(data['values'][1])
    mod_az= abs(data['values'][2])
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
