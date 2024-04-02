from repositories.task_repository import TaskRepository
from repositories.user_repository import UserRepository
import datetime


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
        else:
            return False
    
    def create_user(self, username, password):
        if self.user_repository.add_user(username, password):
            return True
        else:
            return False
        
    def add_task_to_repository(self, title, details, date):
        if self.user != None:
            repodate = f"{date.year}-{date.month}-{date.day}"
            self.task_repository.add_task(self.user, title, details, repodate)
            return True
        else:
            return False
    
    def get_tasks_from_repository(self):
        if self.user != None:
            tasks = self.task_repository.get_tasks_by_username(self.user)
            self.retrieved_tasks = tasks
            return True
        else:
            return False

        
    def task_to_done(self, id):
        if self.retrieved_tasks == None:
            return False
        for task in self.retrieved_tasks:
            if id == task[0]:
                self.task_repository.change_task_to_done(id)
                self.get_tasks_from_repository()
                break 
        else:
            return False

    def remove_task_from_db(self, id):
        if self.retrieved_tasks == None:
            return False
        for task in self.retrieved_tasks:
            if id == task[0]:
                self.task_repository.remove_task(id)
                self.get_tasks_from_repository()
                return True
        return False
    
    def return_user_tasks_by_date(self, date):
        today_tasks = []
        for task in self.retrieved_tasks:
            if task[4] == f"{date.year}-{date.month}-{date.day}":
                today_tasks.append(task)
        print(today_tasks)
        return today_tasks

    
