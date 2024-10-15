import app_types
from task_interfaces import transcript_task, summary_chained_task, call_callback_chained_task
import celery
import config


def transcript_and_summary_service(params: app_types.TranscriptAndSummaryParams) -> celery.Task:
    return celery.chain(
        transcript_task.s(app_types.TaskTranscriptParams(audio_url=params.audio_url)),
        summary_chained_task.s(),
        call_callback_chained_task.s(callback_params=app_types.TaskCallCallbackParams2(callback_url=params.callback_url, callback_data=params.callback_data)) 
    )()


print("calling transcribe_and_summary_service")
res = transcript_and_summary_service(app_types.TranscriptAndSummaryParams(audio_url=config.audio_url, callback_url=config.callback_url, callback_data=config.callback_data))
# dump the result of a celery delay call
print(f"waiting for result of task: {res.task_id}")
print(f"result: {res.get()}")
print(f"graph: {res.parent.parent.graph}")

