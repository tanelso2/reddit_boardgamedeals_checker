import configparser
from datetime import date
import os
from twilio.rest import TwilioRestClient

class TwilioMessenger():
    def __init__(self, config_dir=None):
        mydir = os.path.abspath(os.path.dirname(__file__))
        self.config_dir = config_dir or mydir


        config = configparser.ConfigParser()
        config.read(os.path.join(self.config_dir, "twilio.ini"))
        twilio_account_sid = config["Twilio"]["AccountSID"]
        twilio_auth_token= config["Twilio"]["AuthToken"]

        self.cell_number = config["Twilio"]["CellNumber"]
        self.twilio_number = config["Twilio"]["TwilioNumber"]

        self.client = TwilioRestClient(twilio_account_sid, twilio_auth_token)


    def send_message(self, reddit_post, board_game):
        message = f"""
{board_game.upper()}
{self.format_date(reddit_post)}
{reddit_post.title}
{reddit_post.shortlink}"""
        self.client.messages.create(
            to=self.cell_number,
            from_=self.twilio_number,
            body=message
        )

    def format_date(self, reddit_post):
        created = date.fromtimestamp(reddit_post.created)
        return created.strftime('%Y/%m/%d')

