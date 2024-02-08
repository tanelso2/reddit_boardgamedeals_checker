from checker.checkers.base import RedditChecker
import logging

def get_list_of_games():
    return ["scythe", "avatar", "revive"]

def is_game_in_post(post, board_game):
    return board_game in post.title.lower() or board_game in post.selftext.lower()

def get_game_in_post(post, games):
    for game in games:
        if is_game_in_post(post, game):
            return game
    return None

class BoardGameChecker(RedditChecker):
    def __init__(self, db_file, config_dir):
        super().__init__(db_file, config_dir, "boardgamedeals")
        self.games = get_list_of_games()

    def pred(self, post):
        game = get_game_in_post(post, self.games)
        return game is not None

    def after(self, post):
        game = get_game_in_post(post, self.games)
        logging.info(f"Found {game} in post {post}")

