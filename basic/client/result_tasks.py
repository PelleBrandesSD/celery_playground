from celery import Celery
result_client = Celery('result_tasks', broker='redis://localhost:6379/2', backend='redis://localhost:6379/3', namespace='result_tasks')    
 
#client.conf.task_routes = {'tasks.add': {'queue': 'tasks'}}


@result_client.task(name='tasks.add_result_handler', queue='results')
def add_result_handler(result, calculate_id) -> dict:
    pass


