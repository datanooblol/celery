# celery
A repo for studying celery for distributed workers  

## Observed Behaviors
- if using shared_task, here in my stack, it always break
- if registering tasks manually, it's mostly controllable. It hardly breaks
- when using celery_app.task(name="register.your.function.name"), this one help you to delegate, track and retrieve results more easily
