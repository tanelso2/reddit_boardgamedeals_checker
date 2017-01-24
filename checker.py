#!/usr/bin/env python3
import configparser
import database
import messaging
import praw
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

wishlist_loc = os.path.join(mydir, "wishlist.txt")
with open(wishlist_loc, 'r') as f:
    data = f.read().split('\n')
    data.remove("")
    wishlist = [s.lower() for s in data]


def is_game_in_post(post, board_game):
    return board_game in post.title.lower() or board_game in post.selftext.lower()

for s in submissions:
    for board_game in wishlist:
        if is_game_in_post(s, board_game) and not database.is_post_in_db(s):
            messaging.send_message(s, board_game)
            database.insert_post(s)

database.done()
