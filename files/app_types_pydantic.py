from pydantic import BaseModel
from typing import Any, Dict, Optional

# base classes for all task results

class TaskMeta(BaseModel):
    task_id: str
    name: str
    queue: str


class TaskParams(BaseModel):
    pass


class TaskResponseMeta(BaseModel):
    task: Optional[TaskMeta] = None
    params: Optional[TaskParams] = None # params first argument
    params2: Optional[TaskParams] = None # extra params when chaining tasks (second argument)

TaskResult = Any


class TaskResponse(BaseModel):
    result: TaskResult
    meta: TaskResponseMeta
    
# task specific classes

class TaskTranscriptParams(TaskParams):
    audio_url: str


class TaskTranscriptResponseMeta(TaskResponseMeta):
    params: TaskTranscriptParams


class TaskTranscriptResponse(TaskResponse):
    result: str
    meta: TaskTranscriptResponseMeta
    
class TaskSummaryParams(TaskParams):
    text: str

class TaskSummaryResponseMeta(TaskResponseMeta):
    params: TaskTranscriptResponse | dict[str, Any]
    

class TaskSummaryResponse(TaskResponse):
    result: str
    meta: TaskSummaryResponseMeta


class TranscriptAndSummaryParams(BaseModel):
    audio_url: str
    callback_url: str
    callback_data: Dict[str, Any]
    

class TaskCallCallbackParams2(TaskParams):
    callback_url: str
    callback_data: Dict[str, Any]


class TaskCallCallbackResponseMeta(TaskResponseMeta):
    params: Any
    params2: TaskCallCallbackParams2
    

class TaskCallCallbackResponse(TaskResponse):
    result: Optional[Dict[str, Any]] = None
    meta: TaskCallCallbackResponseMeta


class TranscriptAndSummaryResult(BaseModel):
    transcript: TaskTranscriptResponse
    summary: TaskSummaryResponse
    meta: TaskResponseMeta