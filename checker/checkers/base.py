import configparser
import logging
import os
import praw
import checker.db.database as database

def get_reddit_client(config_dir):
    config = configparser.ConfigParser()
    config.read(os.path.join(config_dir, "reddit.ini"))
    reddit_client_id = config["Reddit"]["ClientId"]
    reddit_client_secret = config["Reddit"]["ClientSecret"]
    reddit_username = config["Reddit"]["Username"]
    reddit_user_agent = f"python:redditchecker:1.0 (by /u/{reddit_username})"

    reddit = praw.Reddit(client_id=reddit_client_id,
                         client_secret=reddit_client_secret,
                         user_agent=reddit_user_agent)
    return reddit

class RedditChecker():
    def __init__(self, db_file, config_dir, subreddit=""):
        self.reddit = get_reddit_client(config_dir)
        self.db = database.RedditPostDatabase(db_file=db_file)
        self.subreddit = subreddit

    @property
    def check_name(self):
        return self.__class__.__name__

    def get_posts(self):
        return self.reddit.subreddit(self.subreddit).new(limit=100)

    def pred(self, post):
        return True

    def after(self, post):
        logging.info(f"Found post for check {self.check_name}: {post}")

    def check_submissions(self):
        logging.info(f"Checking submissions for check {self.check_name}")
        posts = self.get_posts()
        posts = list(posts)
        logging.info(f"Got {len(posts)} posts")
        for s in posts:
            if self.pred(s) and not self.db.is_post_in_db(s):
                logging.debug(f"Adding post id {s.id} to database")
                self.db.insert_post(s)
                self.after(s)
