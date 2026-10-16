"""
Task execution worker service with retry backoff and failure handlers.
"""

import time
import logging
from typing import Optional
from .models import Task, TaskRepository
from .notifications import EmailNotifier, SlackNotifier

logger = logging.getLogger(__name__)

class TaskWorkerService:
    def __init__(self, repo: TaskRepository, email_notifier: EmailNotifier, slack_notifier: Optional[SlackNotifier] = None):
        self.repo = repo
        self.email_notifier = email_notifier
        self.slack_notifier = slack_notifier

    def process_task(self, task_id: str) -> bool:
        task = self.repo.find_by_id(task_id)
        if not task:
            raise ValueError(f"Task with id {task_id} not found")

        task.status = "in_progress"
        self.repo.save(task)

        try:
            self._execute_job(task)
            task.status = "completed"
            self.repo.save(task)
            return True
        except Exception as exc:
            return self._handle_task_failure(task, exc)

    def _execute_job(self, task: Task):
        # Actual task execution workload simulation
        if "critical_job" in task.title:
            raise RuntimeError("Database connection timed out during execution")

    def _handle_task_failure(self, task: Task, error: Exception) -> bool:
        """Handles task retry logic and sends failure alerts when max retries are exceeded."""
        task.retry_count += 1
        if task.retry_count <= task.max_retries:
            task.status = "pending"
            backoff_delay = 2 ** task.retry_count
            time.sleep(backoff_delay)
            self.repo.save(task)
            return False

        task.status = "failed"
        self.repo.save(task)

        # Notify admin of dead-letter / failure state
        if task.assigned_to:
            self.email_notifier.send_notification(
                recipient=task.assigned_to,
                subject=f"Task Failed: {task.title}",
                message_body=f"Task {task.task_id} failed after {task.retry_count} retries. Error: {error}"
            )
        return False
