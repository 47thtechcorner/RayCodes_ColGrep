"""
Data models and in-memory repository for tasks and user records.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import uuid

@dataclass
class User:
    user_id: str
    email: str
    username: str
    role: str = "member"  # admin, member, viewer

@dataclass
class Task:
    task_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    title: str = ""
    description: str = ""
    assigned_to: Optional[str] = None
    status: str = "pending"  # pending, in_progress, completed, failed
    retry_count: int = 0
    max_retries: int = 3
    created_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None

class TaskRepository:
    def __init__(self):
        self._tasks: dict[str, Task] = {}

    def save(self, task: Task) -> Task:
        self._tasks[task.task_id] = task
        return task

    def find_by_id(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)

    def find_by_status(self, status: str) -> List[Task]:
        return [t for t in self._tasks.values() if t.status == status]

    def list_all(self) -> List[Task]:
        return list(self._tasks.values())
