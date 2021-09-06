import os

from celery import Celery, platforms
# from django.conf import settings
from celery.utils.log import get_task_logger
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', "application.settings")
django.setup()

if os.environ.get("PYTHONOPTIMIZE", ""):
    print("开始启动")
else:
    print("\33[31m环境变量问题，Celery Client启动后无法正常执行Ansible任务，\n请设置export PYTHONOPTIMIZE=1；\n\33[32mDjango环境请忽略\33[0m")



celery_logger = get_task_logger(__name__)

app = Celery(f"dvadmin")

# 加载配置 ,指定rabbitmq
# app.config_from_object('application.celery_tasks.config')
app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS,)
app.autodiscover_tasks(['application.celery_tasks.ansible_task.ansible_playbook_api_29', 'application.celery_tasks.test_tasks.test'])
# app.conf.task_send_sent_event = True
# app.conf.worker_send_task_events = True
platforms.C_FORCE_ROOT = True



# celery -A application.celery_tasks.celery worker -P eventlet --loglevel=info#
