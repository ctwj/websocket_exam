# build web socket program with flask-uwsgi-web-socket

## 0x01 what we need?
1. flask
2. flask_uwsgi_websocket
3. python environment
4. uwsgi

## 0x02 what we need do?
use docker
```
$ docker run -itd --name websocket -v ~/Program/websocket:/kerwin -p 8080:8080 python:3.5.4
$ docker exec -it websocket bash
root@0c22401e0a7f:/# pip install Flask-uWSGI-WebSocket
root@0c22401e0a7f:/# pip install gevent
root@0c22401e0a7f:/# cd /kerwin/exam1
root@0c22401e0a7f:/kerwin/exam1# uwsgi --master --http :8080 --http-websockets --wsgi echo:app
```

## 0x03 what we get now?
if everything is ok. now , we can see this page.
![websocket init.png](http://upload-images.jianshu.io/upload_images/5941869-42ce0f357de77b0d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

and when we send a message, we can get two message back
![websocket_exam1.png](http://upload-images.jianshu.io/upload_images/5941869-e889c43ca01c83cb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)







