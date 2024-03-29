import unittest
import datetime
from src.repositories.task_repository import TaskRepository

class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        self.task_repository = TaskRepository("tests.db")
        self.task_repository.clear_all_tasks()
        self.task_repository.add_table_to_db()
    
    def create_date(self):
        taskdate = datetime.datetime.now()
        return f"{taskdate.year}-{taskdate.month}-{taskdate.day}"
    
    def test_add_task(self):
        date = self.create_date()
        self.task_repository.add_task("username", "title", "details", date)
        all_tasks = self.task_repository.get_all_tasks()
        self.assertEqual(all_tasks[0], (1, "username", "title", "details", date, 0))
    
    def test_get_tasks(self):
        date = self.create_date()
        self.task_repository.add_task("a", "title", "details", date)
        self.task_repository.add_task("b", "title", "details", date)
        all_tasks = self.task_repository.get_all_tasks()
        self.assertEqual(all_tasks[0][1], "a")
        self.assertEqual(all_tasks[1][1], "b")

    def test_delete_task(self):
        date = self.create_date()
        self.task_repository.add_task("a", "to be deleted", "details", date)
        all_tasks = self.task_repository.get_all_tasks()
        self.assertEqual(all_tasks, [(1, "a", "to be deleted", "details", date, 0)])
        self.task_repository.remove_task(all_tasks[0][0])
        self.assertEqual(self.task_repository.get_all_tasks(), [])
    
    def test_tasks_by_username(self):
        date = self.create_date()
        self.task_repository.add_task("a", "title", "details", date)
        self.task_repository.add_task("a", "title2", "details2", date)
        user_tasks = self.task_repository.get_tasks_by_username('a')
        self.assertEqual(user_tasks[0], (1, "a", "title", "details", date, 0))
        self.assertEqual(user_tasks[1], (2, "a", "title2", "details2", date, 0))
        
    def test_task_to_done(self):
        date = self.create_date()
        self.task_repository.add_task("a", "title", "details", date)
        self.task_repository.change_task_to_done(1)
        user_tasks = self.task_repository.get_tasks_by_username('a')
        self.assertEqual(user_tasks[0][-1], 1)



    
