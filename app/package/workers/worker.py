# app/package/worker.py
from time import sleep
from package.workers.controller import celery_app

# always register a task, so it can be discovered in the group(...)
# celery_app.task(name="folder.file.function")
@celery_app.task(name="package.workers.worker.add")
def add(x, y):
    sleep(5)  # Simulate long-running task
    return x + y