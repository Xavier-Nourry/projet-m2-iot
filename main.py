from flask import Flask
import http.client, urllib
import requests


app = Flask(__name__)


@app.route("/notify-uplink", methods=['GET', 'POST'])
def notify_uplink():
    r = requests.post("https://api.pushover.net/1/messages.json", data = {
        "token": "afneydpm7t3oxqg64o4vgi7kchjrzk",
        "user": "uspcin8whkjxgveh9oy2ursk24w3vr",
        "message": "Alerte SmartPills : Roger n'a pas pris ses cachets"
    },
    files = {
        "attachment": ("logo.jpg", open("resources/images/logo.jpg", "rb"), "image/jpeg")
    })
    #conn = http.client.HTTPSConnection("api.pushover.net:443")
    #conn.request("POST", "/1/messages.json",
    #urllib.parse.urlencode({
    #    "token": "afneydpm7t3oxqg64o4vgi7kchjrzk",
    #    "user": "uspcin8whkjxgveh9oy2ursk24w3vr",
    #    "message": "Alerte SmartPillBox : Roger n'a pas pris ses cachets",
    #}), { "Content-type": "application/x-www-form-urlencoded" })
    

@app.route("/")
def indx():
    return "<h2>Projet M2 IOT - Pilulier Intelligent</h2>"