from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    if request.method == 'GET':
        return "TODO, GET sensor value"

if __name__ == '__main__':
    app.run()

