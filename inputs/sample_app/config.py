"""
Simple Task Manager & Notification Service
Configuration settings, database connection, and environment variables.
"""

import os
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    host: str = os.getenv("DB_HOST", "localhost")
    port: int = int(os.getenv("DB_PORT", "5432"))
    username: str = os.getenv("DB_USER", "postgres")
    password: str = os.getenv("DB_PASS", "secret")
    database_name: str = "task_manager_db"
    max_connections: int = 20
    timeout_seconds: float = 30.0

@dataclass
class AppConfig:
    app_name: str = "SimpleTaskManager"
    debug_mode: bool = False
    secret_key: str = os.getenv("SECRET_KEY", "super-secret-key-12345")
    api_prefix: str = "/api/v1"
    db_config: DatabaseConfig = DatabaseConfig()

config = AppConfig()
