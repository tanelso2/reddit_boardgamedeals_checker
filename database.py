import sqlite3
con = sqlite3.connect('boardgamedeals.db')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS posts(id TEXT);")
c.execute("CREATE UNIQUE INDEX IF NOT EXISTS postIdIdx ON posts(id);")
con.commit()


def done():
    con.close()

INSERT_STMT = "INSERT OR IGNORE INTO posts VALUES (?)"
def insert_post(post):
    c.execute(INSERT_STMT, (post.id,))
    con.commit()


SELECT_STMT = "SELECT * FROM posts WHERE id LIKE ?"
def is_post_in_db(post):
    c.execute(SELECT_STMT, (post.id,))
    return c.fetchone() is not None

if __name__ == "__main__":
    test_id = "def"
    insert_post(test_id)
    print(is_post_in_db(test_id))
    done()
