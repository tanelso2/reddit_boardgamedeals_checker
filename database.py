import sqlite3
import os

INSERT_STMT = "INSERT OR IGNORE INTO posts VALUES (?)"
SELECT_STMT = "SELECT * FROM posts WHERE id LIKE ?"

class GamesDatabase():
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS posts(id TEXT);")
        self.cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS postIdIdx ON posts(id);")
        self.con.commit()

    def __del__(self):
        self.cursor.close()
        self.con.close()

    def insert_post(self, post):
        self.cursor.execute(INSERT_STMT, (post.id,))
        self.con.commit()


    def is_post_in_db(self, post):
        self.cursor.execute(SELECT_STMT, (post.id,))
        return self.cursor.fetchone() is not None
