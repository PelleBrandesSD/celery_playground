from uuid import uuid4
from tasks import add, add_result_handler, calculate
# from result_tasks import add_result_handler
from celery import chain


def calculate_service(x: int, y: int):
    return calculate.delay(x,y)

def calculate_service_chain(x: int, y: int):
    calculate_id = str(uuid4())
    return chain(
        add.s(x, y),
        add_result_handler.s(calculate_id=calculate_id)
    )()

print("calling calculate_service 1")
result1 = calculate_service_chain(4, 4)
# dump the result of a celery delay call
print(f"waiting for result of task: {result1.task_id}")
print(f"result: {result1.get()}")
