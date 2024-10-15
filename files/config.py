storage_url = "implement me"

broker = "redis://localhost:6379/0"
backend = 'redis://localhost:6379/1'

exchange = "trans_sum_exchange"

callback_queue = "callback_queue"
transcript_queue = "transcript_queue"
summary_queue = "summary_queue"
default_queue = "default_queue"

# callback_queue = "all_queue"
# transcript_queue = "all_queue"
# summary_queue = "all_queue"

task_call_callback = "tasks.call_callback"
task_call_callback_chained = "tasks.call_callback_chained"
task_transcript = "tasks.transcript"
task_transcript_chained = "tasks.transcript_chained"
task_summary = "tasks.summary"
task_summary_chained = "tasks.summary_chained"

callback_app = "callback_tasks"
summary_app = "summary_tasks"
transcript_app = "transcript_tasks"


# the following is just for the example. Should be given by api call or whatever.
base_callback_url = "https://5de5fe61-9663-442b-bf85-7af915d7153d.mock.pstmn.io"
transcript_callback_url = f"{base_callback_url}/transcription"
summary_callback_url = f"{base_callback_url}/summary"
callback_url = f"{base_callback_url}/all"
audio_url = "implement me"
callback_data = {
    "conversation_id": "1234"
}
