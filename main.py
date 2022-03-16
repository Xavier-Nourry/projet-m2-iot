from flask import Flask
import requests


app = Flask(__name__)


@app.route("/notify-uplink", methods=['GET', 'POST'])
def notify_uplink():
    r = requests.post("https://api.pushover.net/1/messages.json", data = {
        "token": "afneydpm7t3oxqg64o4vgi7kchjrzk",
        "user": "uspcin8whkjxgveh9oy2ursk24w3vr",
        "message": "Alerte ! Roger Martinez; 185 Rue de la paix, 73370 Le Bourget-du-lac; 06 45 12 87 58; n'a pas pris ses cachets"
    },
    files = {
        "attachment": ("logo.png", open("resources/images/logo.png", "rb"), "image/png")
    })
    

@app.route("/")
def indx():
    return "<h2>Projet M2 IOT - Pilulier Intelligent</h2>"