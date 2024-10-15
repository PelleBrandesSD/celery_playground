from celery import Task
from app_types import TaskTranscriptParams, TaskSummaryParams, TaskCallCallbackParams2
from task_interfaces import transcript_task, call_callback_task, summary_task
import config


def transcript_service(*, audio_url: str) -> Task:
    return transcript_task.delay(TaskTranscriptParams(audio_url=audio_url))

def summary_service(*, text: str) -> Task:
    return summary_task.delay({"text": text})

def call_callback_service(*, result: dict, callback_url: str, callback_data: dict) -> Task:
    return call_callback_task.delay(result, {
        "callback_url": callback_url, 
        "callback_data": callback_data
        })

print("calling transcript_service")
transcribe_result = transcript_service(audio_url=config.audio_url)
print(f"waiting for result of task: {transcribe_result.task_id}")
print(f"result: {transcribe_result.get()}")

print("calling summary_service")
summarize_result = summary_service(text="This is a test")
print(f"waiting for result of task: {summarize_result.task_id}")
print(f"result: {summarize_result.get()}")

print("calling call_callback_service")
callback_result = call_callback_service(result={"what_ever_prop": "what ever result"}, callback_url=config.callback_url, callback_data=config.callback_data)
print(f"waiting for result of task: {callback_result.task_id}")
print(f"result: {callback_result.get()}")


