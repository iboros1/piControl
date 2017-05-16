#!/usr/bin/env python3.5
from flask import Flask, render_template


app = Flask(__name__)
#app.run(host='0.0.0.0', port='5002')
#wsgi_app = app.wsgi_app

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    hello_world()
