#!/usr/bin/env python3.5
from flask import Flask, render_template
from execute import DEFAULT, hdmi

app = Flask(__name__)
#app.run(host='0.0.0.0', port='5002')
#wsgi_app = app.wsgi_app

@app.route('/')
def hello_world():
    col = DEFAULT[1]
    default = DEFAULT[0]
    return render_template('index.html', state=default, color=col)


@app.route('/button')
def button():
    hdmi(DEFAULT)
    return render_template('index.html')

if __name__ == "__main__":
    hello_world()
