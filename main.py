from flask import Flask, request
from flask import request
import json

app = Flask(__name__)

data = []

@app.route("/notify-uplink", methods=['GET', 'POST'])
def notify_uplink():
    global data
    if request.method == 'POST':
        if request.data:
                rcv_data = json.loads(request.data.decode(encoding='utf-8'))
                if rcv_data: 
                    data.insert(0, rcv_data)
                if len(data) != 0:
                    return data[0]
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
    global data
    to_display = "Projet M2 IOT - Pilulier Intelligent</br></br>"
    if len(data) != 0:
        for item in data:
            to_display += item + "</br>"
    return to_display
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