import configparser
import logging
import os
import requests

homedir = os.path.expanduser("~")

class DiscordMessenger():
    def __init__(self, config_dir=None):
        mydir = os.path.abspath(os.path.dirname(__file__))
        self.config_dir = config_dir or mydir

        config = configparser.ConfigParser()
        config_file = os.path.join(self.config_dir, "discord.ini")
        config.read(config_file)
        self.url = config["Discord"]["URL"]

    def _send_message(self, message):
        requests.post(self.url, json={"content": message})

    def send_message(self, post):
        message = f"""{post.title}\n{post.shortlink}"""
        self._send_message(message)
