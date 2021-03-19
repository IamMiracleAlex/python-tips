import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# crontabs
app.conf.update(
    timezone='Africa/Lagos',
    enable_utc=True,
)

app.conf.beat_schedule = {
      
    "get-published-tips": {
        "task": "tweets.tasks.get_published_tips",
        # "schedule": crontab(minute=0, hour=0)  # every day at midnight
        "schedule": crontab(minute='*/20')  # every 20 mins
    },
}
