from flask import Flask
from calculator_app import app as calculator_app 

app = Flask(__name__)
#app.register_blueprint(calculator_app, url_prefix='/calculator')


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return ''

@app.route("/calculator/add", methods=['POST'])
def add():
    return ''

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return ''

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
