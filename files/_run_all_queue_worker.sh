celery --app tasks_all worker --queues all_queue --loglevel=DEBUG -n transcript_worker@%h -E