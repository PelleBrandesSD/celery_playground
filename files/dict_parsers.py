from app_types_dict import (
    TaskMetaDict, 
    TaskParamsDict, 
    TaskResponseMetaDict, 
    TaskResponseDict, 
    TaskCallCallbackParams2Dict, 
    TaskCallCallbackResponseMetaDict, 
    TaskCallCallbackResponseDict, 
    TaskSummaryParamsDict, 
    TaskSummaryResponseMetaDict, 
    TaskSummaryResponseDict, 
    TaskTranscriptParamsDict, 
    TaskTranscriptResponseMetaDict, 
    TaskTranscriptResponseDict, 
    TranscriptAndSummaryParamsDict, 
    TranscriptAndSummaryResultDict
)
from app_types_pydantic import (
    TaskCallCallbackParams2, 
    TaskMeta, 
    TaskParams, 
    TaskResponseMeta, 
    TaskResponse, 
    TaskSummaryParams, 
    TaskSummaryResponse, 
    TaskTranscriptParams, 
    TaskTranscriptResponse, 
    TaskTranscriptResponseMeta,
    TaskCallCallbackResponseMeta, 
    TaskCallCallbackResponse,
    TranscriptAndSummaryParams, 
    TranscriptAndSummaryResult,
    TaskSummaryResponseMeta
)

# define function parsers for all dict classes to pydantic classes

def task_meta_dict_to_pydantic(task_meta_dict: TaskMetaDict) -> TaskMeta:
    return TaskMeta(**task_meta_dict)

def task_params_dict_to_pydantic(task_params_dict: TaskParamsDict | None) -> TaskParams:
    return TaskParams(**task_params_dict) if task_params_dict else None

def task_response_meta_dict_to_pydantic(task_response_meta_dict: TaskResponseMetaDict) -> TaskResponseMeta:
    return TaskResponseMeta(
        params=task_params_dict_to_pydantic(task_response_meta_dict.get('params')),
        params2=task_params_dict_to_pydantic(task_response_meta_dict.get('params2')),
        task=task_meta_dict_to_pydantic(task_response_meta_dict.get('task'))
    )

def task_response_dict_to_pydantic(task_response_dict: TaskResponseDict) -> TaskResponse:
    return TaskResponse(
        result=task_response_dict.get('result'),
        meta=task_response_meta_dict_to_pydantic(task_response_dict.get('meta'))
    )
    
def task_call_callback_params2_dict_to_pydantic(task_call_callback_params2_dict: TaskCallCallbackParams2Dict) -> TaskCallCallbackParams2:
    return TaskCallCallbackParams2(**task_call_callback_params2_dict)

def task_call_callback_response_meta_dict_to_pydantic(task_call_callback_response_meta_dict: TaskCallCallbackResponseMetaDict) -> TaskCallCallbackResponseMeta:
    return TaskCallCallbackResponseMeta(
        params=task_params_dict_to_pydantic(task_call_callback_response_meta_dict.get('params')),
        params2=task_call_callback_params2_dict_to_pydantic(task_call_callback_response_meta_dict.get('params2')),
        task=task_meta_dict_to_pydantic(task_call_callback_response_meta_dict.get('task'))
    )

def task_call_callback_response_dict_to_pydantic(task_call_callback_response_dict: TaskCallCallbackResponseDict) -> TaskCallCallbackResponse:
    return TaskCallCallbackResponse(
        result=task_call_callback_response_dict.get('result'),
        meta=task_call_callback_response_meta_dict_to_pydantic(task_call_callback_response_dict.get('meta'))
    )
    
def task_summary_params_dict_to_pydantic(task_summary_params_dict: TaskSummaryParamsDict) -> TaskSummaryParams:
    return TaskSummaryParams(**task_summary_params_dict)

def task_summary_response_meta_dict_to_pydantic(task_summary_response_meta_dict: TaskSummaryResponseMetaDict) -> TaskSummaryResponseMeta:
    return TaskSummaryResponseMeta(
        params=task_response_dict_to_pydantic(task_summary_response_meta_dict.get('params')),
        task=task_meta_dict_to_pydantic(task_summary_response_meta_dict.get('task'))
    )
    
def task_summary_response_dict_to_pydantic(task_summary_response_dict: TaskSummaryResponseDict) -> TaskSummaryResponse:
    return TaskSummaryResponse(
        result=task_summary_response_dict.get('result'),
        meta=task_summary_response_meta_dict_to_pydantic(task_summary_response_dict.get('meta'))
    )

def task_transcript_params_dict_to_pydantic(task_transcript_params_dict: TaskTranscriptParamsDict) -> TaskTranscriptParams:
    return TaskTranscriptParams(**task_transcript_params_dict)

def task_transcript_response_meta_dict_to_pydantic(task_transcript_response_meta_dict: TaskTranscriptResponseMetaDict) -> TaskTranscriptResponseMeta:
    return TaskTranscriptResponseMeta(
        params=task_transcript_params_dict_to_pydantic(task_transcript_response_meta_dict.get('params')),
        task=task_meta_dict_to_pydantic(task_transcript_response_meta_dict.get('task'))
    )

def task_transcript_response_dict_to_pydantic(task_transcript_response_dict: TaskTranscriptResponseDict) -> TaskTranscriptResponse:
    return TaskTranscriptResponse(
        result=task_transcript_response_dict.get('result'),
        meta=task_transcript_response_meta_dict_to_pydantic(task_transcript_response_dict.get('meta'))
    )

def transcript_and_summary_params_dict_to_pydantic(transcript_and_summary_params_dict: TranscriptAndSummaryParamsDict) -> TranscriptAndSummaryParams:
    return TranscriptAndSummaryParams(**transcript_and_summary_params_dict)

def transcript_and_summary_result_dict_to_pydantic(transcript_and_summary_result_dict: TranscriptAndSummaryResultDict) -> TranscriptAndSummaryResult:
    return TranscriptAndSummaryResult(
        transcript=task_transcript_response_dict_to_pydantic(transcript_and_summary_result_dict.get('transcript')),
        summary=task_summary_response_dict_to_pydantic(transcript_and_summary_result_dict.get('summary')),
        meta=task_response_meta_dict_to_pydantic(transcript_and_summary_result_dict.get('meta'))
    )   