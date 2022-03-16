from flask import Flask
import http.client, urllib


app = Flask(__name__)


@app.route("/notify-uplink", methods=['GET', 'POST'])
def notify_uplink():
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": "afneydpm7t3oxqg64o4vgi7kchjrzk",
        "user": "uspcin8whkjxgveh9oy2ursk24w3vr",
        "message": "Alerte SmartPillBox : Roger n'a pas pris ses cachets",
    }), { "Content-type": "application/x-www-form-urlencoded" })
    #conn.getresponse()


@app.route("/")
def indx():
    return "<h2>Projet M2 IOT - Pilulier Intelligent</h2>"