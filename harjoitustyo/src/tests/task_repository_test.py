import unittest
from src.repositories.task_repository import TaskRepository

class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        self.task_repository = TaskRepository("tests.db")
        self.task_repository.clear_all_tasks()
        self.task_repository.add_table_to_db()
    
    def test_add_task(self):
        self.task_repository.add_task("username", "title", "details", 0)
        all_tasks = self.task_repository.get_all_tasks()
        self.assertEqual(all_tasks[0], (1, "username", "title", "details", 0, 0))
    
    def test_get_tasks(self):
        self.task_repository.add_task("a", "title", "details", 0)
        self.task_repository.add_task("b", "title", "details", 0)
        all_tasks = self.task_repository.get_all_tasks()
        self.assertEqual(all_tasks[0][1], "a")
        self.assertEqual(all_tasks[1][1], "b")

    
