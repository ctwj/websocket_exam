#!/usr/bin/env python
from flask import Flask, render_template
from flask_uwsgi_websocket import WebSocket

app = Flask(__name__)
ws = WebSocket(app)

@app.route('/')
def index():
    return render_template('index.html')

@ws.route('/websocket')
def echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send("ok, i got mess from html,and i return it back:".encode("utf-8")+msg)
            ws.send("ok, i send message to html, can you see me? ")
        else: return

if __name__ == '__main__':
    app.run(debug=True, threads=16)
