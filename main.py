from flask import Flask, render_template, request, Response
import json
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("sign-in-page.html")


@app.route('/dash', methods=['GET', 'POST'])
def dashboard():
    if request.method == "POST":
        username = request.json['username']
        password = request.json['password']

    return render_template("dashboard.html")


@app.route('/user')
def user_Data():
    return render_template("user_Data.html")


@app.route('/testConnection')
def testConn():
    # r = requests.get('http://localhost:8090/client/testservice')
    # return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

    r = requests.get('http://localhost:8090/printHelloWorldWeb')
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")


if __name__ == "__main__":
    app.run(debug=True)
