"""Gerenciador de tarefas simples — exemplo de código gerado pelo Claude Code."""
from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool = False


class TaskManager:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add(self, title: str) -> Task:
        task = Task(title=title)
        self._tasks.append(task)
        return task

    def complete(self, title: str) -> bool:
        for task in self._tasks:
            if task.title == title:
                task.done = True
                return True
        return False

    def pending(self) -> list[Task]:
        return [t for t in self._tasks if not t.done]

    def all(self) -> list[Task]:
        return list(self._tasks)
