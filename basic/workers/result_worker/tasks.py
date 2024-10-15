from celery import Celery
import logging


result_app = Celery('result_tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1', broker_connection_retry_on_startup=True)    

@result_app.task(name='tasks.add_result_handler', queue='results')
def add_result_handler(result: int, calculate_id: str) -> dict:
    # here we would call callback url to send the result
    return {
        'worker': 'result_worker',
        'result': result, 
        'calculate_id': calculate_id
    }
