from checker.checkers.base import RedditChecker

class StorageDealsChecker(RedditChecker):
    def __init__(self, db_file, config_dir):
        super().__init__(db_file, config_dir, "storage_deals", "buildapcsales")

    def pred(self, post):
        return "[HDD]" in post.title or "[SSD]" in post.title
