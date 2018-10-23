import time
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/post', methods=["POST"])
def postJsonHandler():
    return ''

@app.route('/', methods=["GET"])
def get():
    return render_template('index.html') 


