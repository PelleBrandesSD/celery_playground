from get_celery_app import get_celery_app
import config
   

from tasks_callback import call_callback_chained_task, call_callback_task
from tasks_summary import summary_chained_task, summary_task
from tasks_transcript import transcript_chained_task, transcript_task

app = get_celery_app(config.transcript_app)  

__all__ = [
    "app",
    "call_callback_chained_task",
    "call_callback_task",
    "summary_chained_task",
    "summary_task",
    "transcript_chained_task",
    "transcript_task"
]