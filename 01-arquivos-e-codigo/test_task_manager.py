import unittest

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        tm = TaskManager()
        task = tm.add("Comprar pão")
        self.assertEqual(task.title, "Comprar pão")
        self.assertFalse(task.done)

    def test_complete_task(self):
        tm = TaskManager()
        tm.add("Estudar Claude Code")
        self.assertTrue(tm.complete("Estudar Claude Code"))
        self.assertEqual(tm.pending(), [])

    def test_complete_missing_task_returns_false(self):
        tm = TaskManager()
        self.assertFalse(tm.complete("Não existe"))

    def test_pending_only_returns_incomplete(self):
        tm = TaskManager()
        tm.add("Tarefa A")
        tm.add("Tarefa B")
        tm.complete("Tarefa A")
        pending_titles = [t.title for t in tm.pending()]
        self.assertEqual(pending_titles, ["Tarefa B"])


if __name__ == "__main__":
    unittest.main()
