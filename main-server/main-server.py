from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='', static_folder='static')
with sqlite3.connect("earthquake_data.db") as con:
    cur = con.cursor()
    cur.execute("INSERT INTO Acceleration (X_dir,Y_dir,Z_dir)\
              VALUES (?,?,?)", (1, 1, 1))
    con.commit()
    msg = "Record successfully added"


@app.route('/post', methods=["POST"])
def postJsonHandler():
    data = request.get_json()
    ax = data['values'][0]
    ay = data['values'][1]
    az = data['values'][2]
    print(ax, ay, az)
    with sqlite3.connect("earthquake_data.db") as con:
        print(ax, ay, az)
        cur = con.cursor()
        cur.execute("INSERT INTO Acceleration (X_dir,Y_dir,Z_dir)\
               VALUES (?,?,?)", (ax, ay, az))
        con.commit()
        msg = "Record successfully added"
    return ''


@app.route('/', methods=["GET"])
def get():
    return render_template('index.html')


@app.route("/chart", methods=["GET"])
def chart():
    with sqlite3.connect("earthquake_data.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Acceleration ")
        rows = cur.fetchall()
        print(rows)
        labels = []
        values = []
        for row in rows:
            values = values + [row[0], ]
            labels = labels + [row[3], ]
    return render_template('chart.html', values=values, labels=labels)


app.run(host='0.0.0.0', port=80, debug=True)
