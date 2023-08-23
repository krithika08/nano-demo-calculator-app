from flask import Blueprint,Flask, request, jsonify

app = Flask(__name__)
#calculator_app = Blueprint('calculator_app', __name__)

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json  # Get the JSON data from the request
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    if num1 is None or num2 is None:
        return jsonify({"error": "Both 'num1' and 'num2' must be provided"}), 400

    result = num1 + num2
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello, welcome to the calculator app!"

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    if num1 is None or num2 is None:
        return jsonify({"error": "Both 'num1' and 'num2' must be provided"}), 400

    result = num1 - num2
    return jsonify({"result": result})