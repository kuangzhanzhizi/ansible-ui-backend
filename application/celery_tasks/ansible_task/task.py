from conf.env import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, ansible_result_redis_db,  result_db
from application.celery_tasks.main import app
from apps.ansibleops.utils.ansible_api_v2 import *
from apps.manager.models import Host
from apps.ansibleops.models import AnsibleTasks


import datetime
import os
from celery.app.task import Task
from django.conf import settings


class MyTask(Task):  #毁掉
    abstract = True

    # 任务返回结果后执行
    def after_return(self, status, respose, celery_id, args, *k, **kw):
        r = redis.Redis(host=REDIS_HOST, password=REDIS_PASSWORD, port=REDIS_PORT, db=ansible_result_redis_db)
        a = redis.Redis(host=REDIS_HOST, password=REDIS_PASSWORD, port=REDIS_PORT, db=result_db)
        tid, playbook, group_name, exec_ip = args
        print('MyTask: 处理 Ansible 任务结果， AnsibleID: %s, %s, %s, %s, %s, %s, %s'% (tid,  status, respose, celery_id, args, k, kw))
        rlist = r.lrange(tid, 0, -1)
        try:
            at = AnsibleTasks.objects.filter(ansible_id=tid)[0]
            at.ansible_result = json.dumps([json.loads(i.decode()) for i in rlist])
            ct = a.get('celery-task-meta-%s' % at.celery_id).decode()
            at.celery_result = ct
            at.playbook = playbook
            at.group_name = group_name
            at.save()
            print("同步结果至db: syncAnsibleResult !!!!!: parent_id: %s" % self.request.get('parent_id'), a, kw)
        except:
            pass
        print("%s - %s - %s - %s - %s - %s" % (status, respose, celery_id, args, k, kw))

    # 任务成功后执行
    def on_success(self, retval, task_id, args, kwargs):
        print("执行成功 notice from on_success")
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    # 任务失败时执行
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("执行失败 notice from on_failure")
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)


def get_inventory(exec_ip):
    data = []
    for ip in exec_ip:
        hs = Host.objects.filter(conn_ip=ip)
        for h in hs:
            gs = [i.group_name for i in h.groups.all()]
            data.append({
                'ip': h.conn_ip,
                'username': h.ansible_user,
                'password': h.ansible_pwd,
                'private_key': h.ssh_key,
                'groups': gs
            })
    return data


@app.task(bind=True, base=MyTask)
def ansible_playbook_api_29(self, tid, playbooks, extra_vars, exec_ip, **kw):
    """tid 必须传入，不能生成"""
    # psources = kw.get('sources') or extra_vars.get('sources') or sources
    if isinstance(playbooks, str):
        # playbooks = os.path.join(settings.MEDIA_ROOT, 'system' % playbooks )
        playbooks = ['media/system/playbook/%s' % playbooks]
    inventory = get_inventory(exec_ip)
    AnsiblePlaybookExecApi29(tid, playbooks, inventory, extra_vars)
    return 'ok'
    # data = [
    #     {'ip': '127.0.0.1', }
    # ]
    # AnsiblePlaybookExecApi29(
    #     'AnsiblePlaybook_%s' % datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
    #     ['/Users/chiyingxiong/Project/django-vue-admin/ansible-ui-backend/playbooks/test_debug.yml'],
    #     data, {}
    # )
    # return 'ok'

if __name__ == "__main__":
    app.worker_main()
