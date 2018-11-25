from flask import Flask,jsonify,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class Helloworld(Resource):
    def get(self):
        return jsonify({"about" : "Hello world"})

    def post(self):
        input = request.get_json()
        return jsonify({"result" : input})

class Multiply(Resource):
    def get(self,num):
        return jsonify({"result" : num * 10})

api.add_resource(Helloworld, '/')
api.add_resource(Multiply, "/multiply/<int:num>")

if __name__ == "__main__":
    app.run(debug=True)
