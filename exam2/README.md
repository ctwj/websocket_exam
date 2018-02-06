1. install tornado
`pip install tornado`

2. server side code
```
#-*- encoding:utf-8 -*-
#file: ws.py
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        pass

    def on_message(self, message):
        self.write_message(u"Your message was: "+message)

    def on_close(self):
        pass

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexPageHandler),
            (r'/ws', WebSocketHandler)
        ]

        settings = { "template_path": "."}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()

'''
python ws_app.py
'''
```

3. client side code 
```
<!doctype html>
<head>
    <meta charset="utf-8" />
    <title>WebSocket Echo Example</title>

    <style>
        li { list-style: none; }
    </style>

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>
    <script>
        $(document).ready(function() {
            if (!window.WebSocket) {
                if (window.MozWebSocket) {
                    window.WebSocket = window.MozWebSocket;
                } else {
                    $('#messages').append("<li>Your browser doesn't support WebSockets.</li>");
                }
            }
            var ws = new WebSocket('ws://127.0.0.1:5000/websocket');
            ws.onopen = function(evt) {
                $('#messages').append('<li>WebSocket connection opened.</li>');
            }
            ws.onmessage = function(evt) {
                $('#messages').append('<li>' + evt.data + '</li>');
            }
            ws.onclose = function(evt) {
                $('#messages').append('<li>WebSocket connection closed.</li>');
            }
            $('#send').submit(function() {
                ws.send($('input:first').val());
                $('input:first').val('').focus();
                return false;
            });
        });
    </script>
</head>
<body>
    <h2>WebSocket Echo Example</h2>
    <form id="send" action='.'>
        <input type="text" value="message" />
        <input type="submit" value="Send" />
    </form>
    <div id="messages"></div>
</body>
</html>
```

4. start server
`python ws.py`

5. Effect
![websocket.gif](http://upload-images.jianshu.io/upload_images/5941869-5000b2ef6b916643.gif?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
