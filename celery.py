import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventr.settings')
app = Celery('eventr')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
