from celery import Task
from celery.utils.log import get_task_logger
from services import summarize
from celery.files.app_types_pydantic import TaskSummaryResponse, TaskSummaryResponseMeta, TaskResponse, TaskSummaryParams
from app_utils import get_task_meta
from get_celery_app import get_celery_app
import config
app = get_celery_app(config.transcript_app)    

logger = get_task_logger(__name__)

def _summary(task: Task, text: str) -> TaskSummaryResponse:
    try:
        summary = summarize(text=text)
        return TaskSummaryResponse(
            result=summary,
            meta=TaskSummaryResponseMeta(
                task=get_task_meta(task),
                params=TaskSummaryParams(text=text)
            )
        )
    except Exception as e:
        logger.error(f"Error: {e}")

@app.task(name=config.task_summary, pydantic=True, bind=True, queue=config.summary_queue)
def summary_task(self: Task, params: TaskSummaryParams) -> TaskSummaryResponse:
    return _summary(task=self, text=params.text)

@app.task(name=config.task_summary_chained, pydantic=True, bind=True, queue=config.summary_queue)
def summary_chained_task(self: Task, params: TaskResponse) -> TaskSummaryResponse:
    return _summary(task=self, text=params.result)