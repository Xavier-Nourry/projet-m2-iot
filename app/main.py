from flask import Flask
from flask import request
import json

app = Flask(__name__)

def post_actions(data):
    print(data)
    return data

@app.route("/", methods=['GET', 'POST'])
def indx():
    if request.method == 'POST':
        if request.data:
            rcv_data = json.loads(request.data.decode(encoding='utf-8'))
            rsp = post_actions(rcv_data)
            if rsp:
                return rsp
            else:
                return '200'
        else:
            return '404'

if __name__ == "__main__":
    app.run(host='localhost', port='43560')