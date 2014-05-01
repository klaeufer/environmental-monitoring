import os
from flask import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def default():
    if request.method == 'POST':
        return "you posted!"
    if request.method == 'GET':
        return "GET, good job!"
