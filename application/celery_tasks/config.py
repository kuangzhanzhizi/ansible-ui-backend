from conf.env import BACKEND, BROKER


## 设置 Broker
BROKER_URL = BROKER

## 设置任务结果保存地址
CELERY_RESULT_BACKEND = BACKEND

## celery启动时加载的模块
# CELERY_IMPORTS = ('myapp.tasks', )

## 设置时区
CELERY_TIMEZONE = 'Asia/Shanghai'

## 设置保存时间
CELERY_TASK_RESULT_EXPIRES = 18000  # 18000 秒
