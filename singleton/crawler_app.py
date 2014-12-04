from flask import Flask, render_template, request
from crawler import *
app = Flask(__name__)
#BANK = Bank()

@app.route('/')
def hello_world():
    return "Hello World"
if __name__ == '__main__':
    app.run(debug=True)
