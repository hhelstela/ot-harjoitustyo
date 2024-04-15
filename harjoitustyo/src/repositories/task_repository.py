import sqlite3


class TaskRepository:
    def __init__(self, dbname):
        self.db = sqlite3.connect(dbname)
        self.db.isolation_level = None
        try:
            self.db.execute("CREATE TABLE Tasks (id INTEGER PRIMARY KEY, username TEXT, title TEXT, details TEXT, date DATE, done INTEGER)")
        except:
            pass

    def add_task(self, username, title, details, date, done=0):
        self.db.execute("INSERT INTO Tasks (username, title, details, date, done) VALUES (?, ?, ?, ?, ?)", [
                        username, title, details, date, done])
        return True

    def get_tasks_by_username(self, username):
        user_tasks = self.db.execute(
            "SELECT * FROM Tasks WHERE username=?", [username]).fetchall()
        return user_tasks

    def get_all_tasks(self):
        all_tasks = self.db.execute("SELECT * FROM Tasks").fetchall()
        return all_tasks

    def clear_all_tasks(self):
        self.db.execute("DROP TABLE Tasks")

    def add_table_to_db(self):
        self.db.execute(
            "CREATE TABLE Tasks (id INTEGER PRIMARY KEY, username TEXT, title TEXT, details TEXT, date INTEGER, done INTEGER)")

    def change_task_to_done(self, task_id):
        self.db.execute("UPDATE Tasks SET done = 1 WHERE id=(?)", [task_id])

    def remove_task(self, task_id):
        self.db.execute("DELETE FROM Tasks WHERE id=(?)", [task_id])
