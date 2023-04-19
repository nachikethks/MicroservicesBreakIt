from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)



@app.route('/', methods=['POST', 'GET'])
def index():
	try:
		number_1 = int(request.form.get("first"))
		number_2 = int(request.form.get('second'))
	except:
		number_1 = 0
		number_2 = 0
	operation = request.form.get('operation')
	result = 0
	if operation == 'add':
		response = requests.get('http://microservices_add-service_1:5051/add', json={'num1': number_1, 'num2': number_2})
		result = response.json()
		result = result['result']
	elif operation == 'minus':
		response = requests.get('http://microservices_sub-service_1:5052/sub', json={'num1': number_1, 'num2': number_2})
		result = response.json()
		result = result['result']
	elif operation == 'multiply':
		response = requests.get('http://microservices_mul-service_1:5053/mul', json={'num1': number_1, 'num2': number_2})
		result = response.json()
		result = result['result']
	elif operation == 'divide':
		response = requests.get('http://microservices_div-service_1:5054/div', json={'num1': number_1, 'num2': number_2})
		result = response.json()
		result = result['result']
	elif operation == 'modulus':
		response = requests.get('http://microservices_mod-service_1:5055/mod', json={'num1': number_1, 'num2': number_2})
		result = response.json()
		result = result['result']
	elif operation == 'exponent':
		response = requests.get('http://microservices_exp-service_1:5056/exp', json={'num1': number_1, 'num2': number_2})
		result = response.json()
		result = result['result']
	elif operation == 'equal':
		response = requests.get('http://microservices_equ-service_1:5057/equ', json={'num1': number_1, 'num2': number_2})
		result = response.json()
		result = result['result']
		
	flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

	return render_template('index.html')


if __name__ == '__main__':
	app.run(
		debug=True,
		port=5050,
		host="0.0.0.0"
	)

