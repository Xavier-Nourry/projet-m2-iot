from flask import Flask, request
from flask import request
import json
import http.client, urllib

app = Flask(__name__)

@app.route("/notify-uplink", methods=['GET', 'POST'])
def notify_uplink():
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": "afneydpm7t3oxqg64o4vgi7kchjrzk",
        "user": "uspcin8whkjxgveh9oy2ursk24w3vr",
        "message": "Attention !!! : Roger va mourir",
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    #if request.data:
    #    rcv_data = json.loads(request.data.decode(encoding='utf-8'))
    #    if rcv_data: 
    #        data.insert(0, rcv_data)
    #if request.method == 'POST':
    #    if request.data:
    #            rcv_data = json.loads(request.data.decode(encoding='utf-8'))
    #            if rcv_data: 
    #                data.insert(0, rcv_data)
    #            else:
    #                return '200'
    #    else:
    #        return 'No data passed with the request'
    #elif request.method == 'GET':
    #    return 'Request passed by GET method'
    #else:
    #    return 'Not a valid request'


@app.route("/")
def indx():
    return "<h2>Projet M2 IOT - Pilulier Intelligent</h2>"
    #if request.method:
    #    if request.method == 'POST':
    #        if request.data:
    #            rcv_data = json.loads(request.data.decode(encoding='utf-8'))
    #            rsp = post_actions(rcv_data)
    #            if rsp:
    #                return rsp
    #            else:
    #                return '200'
    #        else:
    #            return 'No data passed with the request'
    #else:
    #    return redirect(url_for('notify-uplink'))