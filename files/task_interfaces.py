import config
from celery import Task
from get_celery_app import get_celery_app
from app_types import TaskCallCallbackParams2, TaskCallCallbackResponse, TaskTranscriptParams, TaskTranscriptResponse, TaskSummaryParams, TaskSummaryResponse, TaskResponse
app = get_celery_app("task_interfaces")   


@app.task(name=config.task_call_callback, pydantic=True, bind=True, queue=config.callback_queue)
def call_callback_task(self: Task, result: dict, callback_params: TaskCallCallbackParams2) -> TaskCallCallbackResponse:
    pass

@app.task(name=config.task_call_callback, pydantic=True, bind=True, queue=config.callback_queue)
def call_callback_chained_task(self: Task, result: TaskResponse, callback_params: TaskCallCallbackParams2) -> TaskCallCallbackResponse:
    pass

@app.task(name=config.task_transcript, pydantic=True, bind=True, queue=config.transcript_queue)
def transcript_task(self: Task, params: TaskTranscriptParams) -> TaskTranscriptResponse:
    pass

@app.task(name=config.task_transcript_chained, pydantic=True, bind=True, queue=config.transcript_queue)
def transcript_chained_task(self: Task, params: TaskResponse) -> TaskTranscriptResponse:
    pass

@app.task(name=config.task_summary, pydantic=True, bind=True, queue=config.summary_queue)
def summary_task(self: Task, params: TaskSummaryParams) -> TaskSummaryResponse:
    pass

@app.task(name=config.task_summary_chained, pydantic=True, bind=True, queue=config.summary_queue)
def summary_chained_task(self: Task, params: TaskResponse) -> TaskSummaryResponse:
    pass

