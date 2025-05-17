# app/package/controller.py
from celery import Celery

celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    result_expires=3600,
)

# this is a manual registration of the task
from package.workers import worker

