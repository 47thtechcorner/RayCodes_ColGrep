# ColGrep Agent Code Search Results

**Query:** where does the application handle task retry backoff and send failure notifications

**Target Scope:** `inputs/sample_app`

## Discovered Code Locations

| Location | Description |
| :--- | :--- |
| `inputs/sample_app/worker.py:40-58` | Exponential retry backoff delay loop and dead-letter failure notification trigger |
| `inputs/sample_app/worker.py:20-34` | Main worker job execution flow and error catch block |
| `inputs/sample_app/models.py:22-25` | Task model retry counter and `max_retries` threshold specification |
| `inputs/sample_app/notifications.py:14-19` | Email dispatcher `send_notification` handler for failure alerts |

```text
inputs/sample_app/worker.py:40-58
inputs/sample_app/worker.py:20-34
inputs/sample_app/models.py:22-25
inputs/sample_app/notifications.py:14-19
```
