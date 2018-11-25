from datetime import datetime
from flask import Flask,jsonify
from flask import request
import json

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1> This is Home Page</h1>"

@app.route("/gettime", methods=["GET","POST","PUT","DELETE","PATCH"])
def get_time():
    # If request is get goes here
    if request.method == 'GET':
        print("Calling GET Method...")
        my_time = str(datetime.now())
        my_string = """
        {
        "current_time" : "my_time"
            
        }
        """.replace("my_time", my_time)
        return my_string

    # If request is post goes here..
    if request.method == 'POST':
        print("Calling POST Method...")
        data = request.json
        print("Received in request:", data)
        test = """
        {
            "Name" : "Test",
            "Age" : "5"
        }
        """
        return test

@app.route("/test/<int:num>")
def mul(num):
    return jsonify({"result" : num * 10})

@app.route("/mypost", methods=['POST'])
def mypost():
    my_value = request.get_json()
    return jsonify({"result" : my_value})


if __name__ == "__main__":
    app.run(debug=True)
    #get_time()
