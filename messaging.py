import configparser
import os
from twilio.rest import TwilioRestClient

mydir = os.path.abspath(os.path.dirname(__file__))

config = configparser.ConfigParser()
config.read(os.path.join(mydir, "twilio.ini"))
twilio_account_sid = config["Twilio"]["AccountSID"]
twilio_auth_token= config["Twilio"]["AuthToken"]
cell_number = config["Twilio"]["CellNumber"]
twilio_number = config["Twilio"]["TwilioNumber"]

client = TwilioRestClient(twilio_account_sid, twilio_auth_token)


def send_message(reddit_post, board_game):
    message = f"\n{board_game.upper()}\n{reddit_post.title}\n{reddit_post.shortlink}"
    client.messages.create(
        to=cell_number,
        from_=twilio_number,
        body=message
    )
