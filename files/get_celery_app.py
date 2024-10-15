from kombu import Exchange, Queue
from celery import Celery
import config


def get_celery_app(app_name: str) -> Celery:
    app = Celery(app_name, broker=config.broker, backend=config.backend, broker_connection_retry_on_startup=True)
    # app.conf.task_queues = (
    #         Queue(config.default_queue, Exchange(config.default_queue), routing_key=config.default_queue),
    #         Queue(config.transcript_queue, Exchange(config.transcript_queue), routing_key=config.transcript_queue),
    #         Queue(config.summary_queue, Exchange(config.summary_queue), routing_key=config.summary_queue),
    #         Queue(config.callback_queue, Exchange(config.callback_queue), routing_key=config.callback_queue)
    #     )
    # app.conf.task_routes = {
    #     'tasks.transcribe': {'queue': config.transcript_queue},
    #     'tasks.summarize': {'queue': config.summary_queue},
    #     'tasks.callback': {'queue': config.callback_queue}
    # }
    # app.conf.task_default_queue = config.default_queue
    # app.conf.task_default_exchange_type = 'direct'
    # app.conf.task_default_routing_key = config.default_queue
    
    return app