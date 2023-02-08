from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'distribution.settings')

app = Celery('djangobin')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # send task every friday 12:00
    'send-mail': {
        'task': 'sender.tasks.send_emails_to_all_subscribers',        
        'schedule': crontab(minute='*/1')# crontab(minute='0', hour='12', day_of_week='fri'),
    },
}