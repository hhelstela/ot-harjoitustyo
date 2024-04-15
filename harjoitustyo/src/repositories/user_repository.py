import sqlite3


class UserRepository:
    def __init__(self, dbname):
        self.db = sqlite3.connect(dbname)
        self.db.isolation_level = None
        try:
            self.db.execute(
                "CREATE TABLE Users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
        except:
            pass

    def add_user(self, username, password):
        usernames_in_db = self.db.execute(
            "SELECT * FROM Users WHERE username=?", [username]).fetchall()
        if len(usernames_in_db) == 0:
            self.db.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [
                            username, password])
            return True
        return False

    def get_all_users(self):
        return (self.db.execute("SELECT * FROM Users").fetchall())

    def login_to_service(self, username, password):
        username_in_db = self.db.execute(
            "SELECT * FROM Users WHERE username=?", [username]).fetchall()
        try:
            if username_in_db[0][-1] == password:
                return True
            return False
        except:
            return False

    def clear_all_users(self):
        self.db.execute("DROP TABLE Users")

    def add_table_to_db(self):
        self.db.execute(
            "CREATE TABLE Users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
