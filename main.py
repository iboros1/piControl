#!/usr/bin/env python3.5
from flask import Flask, render_template,request
from execute import DEFAULT, hdmi

app = Flask(__name__)
#app.run(host='0.0.0.0', port='5002')
#wsgi_app = app.wsgi_app


@app.route('/', methods=['GET', 'POST'])
def tv_status():
    col = DEFAULT[1]
    default = DEFAULT[0]
    if request.method == 'GET':
        return render_template('index.html', state=default, color=col)
    elif request.method == 'POST':
        hdmi(DEFAULT)
        return render_template('index.html', state=default, color=col)

if __name__ == "__main__":
    tv_status()
