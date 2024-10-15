import os
from uuid import uuid4
from celery import Celery, chain
import time

app = Celery('add_tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1', broker_connection_retry_on_startup=True)    

@app.task(name='tasks.add_result_handler', queue='results')
def add_result_handler(result: int, calculate_id: str) -> dict:
    # here we would call callback url to send the result
    return {
        'worker': 'add_worker',
        'result': result, 
        'calculate_id': calculate_id
    }

@app.task(name='tasks.add', queue='calculator')
def add(x: int, y: int) -> int:
    time.sleep(5)
    x = int(x)
    y = int(y)
    result = x + y
    return result
        
@app.task(name='tasks.calculate', queue='calculator')
def calculate(x, y) -> dict:
    calculate_id = str(uuid4())
    result = chain(
        add.s(x, y) |
        add_result_handler.s(calculate_id=calculate_id)
    )
   
    return result.apply_async()
    
