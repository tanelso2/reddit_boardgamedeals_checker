from checker.checkers.base import RedditChecker
from checker.messaging.discord import DiscordMessenger

class StorageDealsChecker(RedditChecker):
    def __init__(self, db_file, config_dir):
        super().__init__(db_file, config_dir, "buildapcsales")
        self.messenger = DiscordMessenger(config_dir=config_dir)

    def pred(self, post):
        return "[HDD]" in post.title or "[SSD]" in post.title

    def after(self, post):
        super().after(post)
        self.messenger.send_message(post)
