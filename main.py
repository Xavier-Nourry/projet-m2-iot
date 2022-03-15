from flask import Flask, request
from flask import request
import json

app = Flask(__name__)

def post_actions(data):
    return data

@app.route("/notify-uplink", methods=['GET', 'POST'])
def notify_uplink():
    if request.method == 'POST':
        if request.data:
                rcv_data = json.loads(request.data.decode(encoding='utf-8'))
                rsp = post_actions(rcv_data)
                if rsp:
                    return rsp
                else:
                    return '200'
        else:
            return 'No data passed with the request'
    elif request.method == 'GET':
        return 'Request passed by GET method'
    else:
        return 'Not a valid request'


@app.route("/")
def indx():
    return "Projet M2 IOT - Pilulier Intelligent"
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