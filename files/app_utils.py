from celery import Task
from celery.files.app_types_pydantic import TaskMeta


def get_task_meta(task: Task) -> TaskMeta:
    try:
        return TaskMeta(
            task_id=task.request.id,
            name=task.name,
            queue=task.queue
        )
    except Exception as e:
        raise e