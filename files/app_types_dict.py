from pydantic import BaseModel
from typing import Any, Dict, Optional

# base classes for all task results

class TaskMetaDict(BaseModel):
    task_id: str
    name: str
    queue: str


class TaskParamsDict(BaseModel):
    pass


class TaskResponseMetaDict(BaseModel):
    task: Optional[TaskMetaDict] = None
    params: Optional[TaskParamsDict] = None # params first argument
    params2: Optional[TaskParamsDict] = None # extra params when chaining tasks Dict(second argument)

TaskResult = Any


class TaskResponseDict(BaseModel):
    result: TaskResult
    meta: TaskResponseMetaDict
    
# task specific classes

class TaskTranscriptParamsDict(TaskParamsDict):
    audio_url: str


class TaskTranscriptResponseMetaDict(TaskResponseMetaDict):
    params: TaskTranscriptParamsDict


class TaskTranscriptResponseDict(TaskResponseDict):
    result: str
    meta: TaskTranscriptResponseMetaDict
    
class TaskSummaryParamsDict(TaskParamsDict):
    text: str

class TaskSummaryResponseMetaDict(TaskResponseMetaDict):
    params: TaskTranscriptResponseDict | dict[str, Any]
    

class TaskSummaryResponseDict(TaskResponseDict):
    result: str
    meta: TaskSummaryResponseMetaDict


class TranscriptAndSummaryParamsDict(BaseModel):
    audio_url: str
    callback_url: str
    callback_data: Dict[str, Any]
    

class TaskCallCallbackParams2Dict(TaskParamsDict):
    callback_url: str
    callback_data: Dict[str, Any]


class TaskCallCallbackResponseMetaDict(TaskResponseMetaDict):
    params: Any
    params2: TaskCallCallbackParams2Dict
    

class TaskCallCallbackResponseDict(TaskResponseDict):
    result: Optional[Dict[str, Any]] = None
    meta: TaskCallCallbackResponseMetaDict


class TranscriptAndSummaryResultDict(BaseModel):
    transcript: TaskTranscriptResponseDict
    summary: TaskSummaryResponseDict
    meta: TaskResponseMetaDict