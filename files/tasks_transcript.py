from celery import Task
from services import transcribe
from get_celery_app import get_celery_app
from celery.files.app_types_pydantic import TaskTranscriptParams, TaskTranscriptResponse, TaskResponse, TaskTranscriptResponseMeta
from app_utils import get_task_meta
import config
app = get_celery_app(config.transcript_app)    

def _transcript(task: Task, audio_url: str) -> TaskTranscriptResponse:
    result = transcribe(audio_url=audio_url)
    return TaskTranscriptResponse( 
            result=result,
            meta= TaskTranscriptResponseMeta(
                task=get_task_meta(task),
                params=TaskTranscriptParams(audio_url=audio_url)
            )
    )

@app.task(name=config.task_transcript, pydantic=True, bind=True, queue=config.transcript_queue)
def transcript_task(self: Task, params: TaskTranscriptParams) -> TaskTranscriptResponse:
    return _transcript(self, audio_url=params.audio_url)

@app.task(name=config.task_transcript_chained, pydantic=True, bind=True, queue=config.transcript_queue)
def transcript_chained_task(self: Task, params: TaskResponse) -> TaskTranscriptResponse:
    return _transcript(self, audio_url=params.result)