from repositories.task_repository import TaskRepository
from repositories.user_repository import UserRepository



class TaskService:
    def __init__(self):
        self.user = None
        self.task_repository = TaskRepository("tasks.db")
        self.user_repository = UserRepository("users.db")
        self.retrieved_tasks = None

    def login(self, username, password):
        if self.user_repository.login_to_service(username, password):
            self.user = username
            self.get_tasks_from_repository()
            return True
        return False

    def create_user(self, username, password):
        if self.user_repository.add_user(username, password):
            return True
        return False

    def add_task_to_repository(self, title, details, date):
        if self.user is not None:
            repodate = f"{date.year}-{date.month}-{date.day}"
            self.task_repository.add_task(self.user, title, details, repodate)
            return True
        return False

    def get_tasks_from_repository(self):
        if self.user is not None:
            tasks = self.task_repository.get_tasks_by_username(self.user)
            self.retrieved_tasks = tasks
            return True
        return False

    def task_to_done(self, task_id):
        if self.retrieved_tasks is None:
            return False
        for task in self.retrieved_tasks:
            if task_id == task[0]:
                self.task_repository.change_task_to_done(task_id)
                self.get_tasks_from_repository()
                break
        return False

    def remove_task_from_db(self, task_id):
        if self.retrieved_tasks is None:
            return False
        for task in self.retrieved_tasks:
            if task_id == task[0]:
                self.task_repository.remove_task(task_id)
                self.get_tasks_from_repository()
                return True
        return False

    def return_user_tasks_by_date(self, date):
        today_tasks = []
        for task in self.retrieved_tasks:
            if task[4] == f"{date.year}-{date.month}-{date.day}":
                today_tasks.append(task)
        return today_tasks
