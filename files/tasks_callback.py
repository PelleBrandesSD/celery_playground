from celery import Task
from celery.utils.log import get_task_logger
from app_types_pydantic import TaskCallCallbackResponse, TaskCallCallbackResponseMeta, TaskResponse, TaskCallCallbackParams2, TaskResponseMeta
from app_types_dict import TaskCallCallbackResponseDict, TaskCallCallbackResponseMetaDict, TaskResponseDict, TaskCallCallbackParams2Dict
import dict_parsers 
from services import call_callback
from app_utils import get_task_meta
from get_celery_app import get_celery_app
import config
app = get_celery_app(config.transcript_app)     

logger = get_task_logger(__name__)

@app.task(name=config.task_call_callback, bind=True, queue=config.callback_queue)
def call_callback_task(self: Task, result: TaskResponseDict, callback_params: TaskCallCallbackParams2Dict) -> TaskCallCallbackResponseDict:
    params = dict_parsers.task_response_dict_to_pydantic(result)
    params2 = dict_parsers.task_call_callback_params2_dict_to_pydantic(callback_params)
    
    try:
        logger.debug(f"Task {self.name} parent: {self.request.parent}")
        callback_result = call_callback(result=params, **params2.model_dump())
        
        response = TaskCallCallbackResponse(
            result=callback_result,
            meta=TaskCallCallbackResponseMeta(
                task=get_task_meta(self),
                params=params,
                params2=params2
            )
        )
        
        return response.model_dump()
    except Exception as e:
        logger.error(f"Error: {e}")
        # TODO: handle errors in tasks
        raise e


@app.task(name=config.task_call_callback_chained, bind=True, queue=config.callback_queue)
def call_callback_chained_task(self: Task, prev_response: TaskResponseDict, callback_params: TaskCallCallbackParams2Dict) -> TaskCallCallbackResponseDict:
    params = dict_parsers.task_response_dict_to_pydantic(prev_response)
    
    try:
        callback_result = call_callback(result=prev_response, callback_params=callback_params)
        
        response = TaskCallCallbackResponse(
            result=callback_result,
            meta=TaskCallCallbackResponseMeta(
                task=get_task_meta(self),
                params=prev_response,
                params2=callback_params
            )
        )
        
        return response
    except Exception as e:
        logger.error(f"Error: {e}")
        # TODO: handle errors in tasks
        raise e

