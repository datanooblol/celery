from celery import Celery
from time import sleep

celery_app = Celery("worker", broker="redis://redis:6379/0", backend="redis://redis:6379/0")

@celery_app.task(name="app.worker.add")
def add(x, y):
    sleep(5)  # Simulate a long-running task
    return x + y
