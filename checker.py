#!/usr/bin/env python3.6
import configparser
import database
import gspread
import messaging
import praw
from oauth2client.service_account import ServiceAccountCredentials
import os

mydir = os.path.abspath(os.path.dirname(__file__))

config = configparser.ConfigParser()
config.read(os.path.join(mydir, "reddit.ini"))
reddit_client_id = config["Reddit"]["ClientId"]
reddit_client_secret = config["Reddit"]["ClientSecret"]
reddit_username = config["Reddit"]["Username"]
reddit_user_agent = f"python:boardgamedealschecker:1.0 (by /u/{reddit_username})"

reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)

submissions = reddit.subreddit("boardgamedeals").new(limit=100)

def get_list_of_games():
    scope = ['https://spreadsheets.google.com/feeds']
    access_key = os.path.join(mydir, "access_key.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(access_key, scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open("Board Games Wishlist")
    records = spreadsheet.worksheet("Sheet1").get_all_records()
    return [ a['Name'].lower() for a in records ]

games = get_list_of_games()

def is_game_in_post(post, board_game):
    return board_game in post.title.lower() or board_game in post.selftext.lower()


for s in submissions:
    for board_game in games:
        if is_game_in_post(s, board_game) and not database.is_post_in_db(s):
            messaging.send_message(s, board_game)
            database.insert_post(s)

database.done()
