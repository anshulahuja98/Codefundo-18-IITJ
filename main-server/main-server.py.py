from flask import Flask, request, render_template
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import sqlite3 as sql
app = Flask(__name__)
db_connect = create_engine('sqlite:///earthquake_data.db')
@app.route('/post', methods=["POST"])
def postJsonHandler():
    data = request.get_json()
    ax= data['values'][0]
    ay= data['values'][1]
    az= data['values'][2]
    try:
        with sql.connect("earthquake_data.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Acceleration (X_dir,Y_dir,Z_dir) 
               VALUES (?,?,?)",(ax,ay,az) )
            con.commit()
            msg = "Record successfully added"
    except:
        con.rollback()
        msg= "error in insert operation"
    return ''
@app.route('/', methods=["GET"])
def get():
    return render_template('index.html') 

