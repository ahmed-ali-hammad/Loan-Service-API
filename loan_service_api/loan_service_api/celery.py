from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loan_service_api.settings')


app = Celery('loan_service_api')

app.config_from_object('django.conf:settings')


# Celery Beat Settings
# app.conf.beat_schedule = {
#     'monthly_payments':{
#         'task': 'api.tasks.pay_loan',
#         'schedule': crontab(hour=7, minute=5),
#     }
# }

app.autodiscover_tasks()

# Debug task
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
