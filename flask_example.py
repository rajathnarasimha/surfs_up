from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world'

@app.route('/<name>', methods=["GET"])
def say_name(name):
    result =  f"Hello {name}"
    return result


@app.route('/add', methods=['GET'])
def add():
    num1 = request.args.get('num1')
    print (f"number 1 :  {num1}")
    num2 = request.args.get('num2')
    print(f"number 2: {num2}")
    result = int(num1) + int (num2)
    return (f"{num1} + {num2} = {result}")
