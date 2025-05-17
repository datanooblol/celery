from fastapi import FastAPI
from .worker import celery_app, add
from celery import group
from celery.result import AsyncResult, GroupResult
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
def read_health():
    return {"message": "alive"}

@app.get("/add")
def read_add():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    r = add.delay(x, y)  # Call the Celery task asynchronously
    return {"task_id": r.id}

@app.get("/task/status/{task_id}")
def get_task_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {"task_status": result.status}

@app.get("/task/result/{task_id}")
def get_task_result(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {"task_result": result.result}

@app.get("/group/add")
def read_group_add():
    jobs = group(add.s(i, i) for i in range(20))
    result = jobs.apply_async()
    result.save()
    return {"task_id": result.id}

@app.get("/group/status/{task_id}")
def get_group_status(task_id: str):
    result = GroupResult.restore(task_id, app=celery_app)
    return {"successful": result.successful()}

@app.get("/group/result/{task_id}")
def get_group_result(task_id: str):
    result = GroupResult.restore(task_id, app=celery_app)
    result.successful()
    return {
        "group_result": result.get()
    }