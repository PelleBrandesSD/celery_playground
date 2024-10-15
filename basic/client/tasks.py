from celery import Celery
client = Celery('add_tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')    

@client.task(name='tasks.add_result_handler', queue='results')
def add_result_handler(result: int, calculate_id: str) -> dict:
    pass

@client.task(name='tasks.add', queue='calculator')
def add(x: int, y: int) -> int:
    pass

@client.task(name='tasks.calculate', queue='calculator')
def calculate(x: int, y: int) -> dict:
    pass
    