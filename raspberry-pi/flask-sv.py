from flask import Flask, request
#curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "username": "fizz bizz"}' http://localhost:8090/post
app = Flask(__name__)


@app.route('/post', methods=["POST"])
def post():
    print(request.data)
    return ''


@app.route('/get', methods=["GET"])
def get():
    return 'GET'


app.run(host='0.0.0.0', port=8090, debug=True)
