import sqlite3

db = sqlite3.connect("users.db")
db.isolation_level = None

class UserRepository:
    def __init__(self):
        try:
            db.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
        except:
            pass
    
    def add_user(self, username, password):
        usernames_in_db = db.execute("SELECT * FROM Users WHERE username=?", [username]).fetchall()
        if len(usernames_in_db) == 0:
            db.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [username, password])
        else:
            return False
    
    def get_users_by_username(self, username):
        usernames = db.execute("SELECT * FROM Users WHERE username=?", [username]).fetchall()
        return(usernames)
    
    def get_all_users(self):
        return(db.execute("SELECT * FROM Users").fetchall())
    
    def login_to_service(self, username, password):
        username_in_db = db.execute("SELECT * FROM Users WHERE username=?", [username]).fetchall()
        try:
            if username_in_db[0][-1] == password:
                return True
            else:
                return False
        except:
            return False

