from entities.task import Task
from entities.user import User
from repositories.task_repository import TaskRepository
from repositories.user_repository import UserRepository

class TaskService:
    def __init__(self):
        self._user = None
        self.task_repository = TaskRepository("tasks")
        self._user_repository = UserRepository()

    def login(self, username, password):
        if self._user_repository.login_to_service(username, password):
            self._user = username
            return True
        else:
            return "Incorrect login credentials"
    
task_service = TaskService()
print(task_service.login("henri", "helstelä"))