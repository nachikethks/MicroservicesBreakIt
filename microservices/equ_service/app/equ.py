from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

class equ(Resource):
    def get(self):
        json = request.json
        return {"result": json['num1']==json['num2']}
    def post(self):
        json = request.json
        return {"result": json['num1']==json['num2']}

api.add_resource(equ, '/equ')

if __name__ == "__main__":
    app.run(
		debug=True,
		port=5057,
		host="0.0.0.0"
	)