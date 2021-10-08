# from django.conf import settings
from django.db.models import CharField, IntegerField, ForeignKey, TextField
from vadmin.op_drf.models import CoreModel


class AnsibleTasks(CoreModel):
    ansible_id = CharField(max_length=80,unique=True, null=True,blank=True)
    celery_id = CharField(max_length=80,unique=True, null=True,blank=True)
    group_name = CharField(max_length=80, null=True, blank=True)
    task_user = CharField(max_length=80, null=True, blank=True)
    playbook = CharField(max_length=80, null=True, blank=True)
    extra_vars = TextField(blank=True, null=True)
    ansible_result = TextField(blank=True)
    celery_result = TextField(blank=True)
    label = CharField(max_length=80, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Ansible任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ansible_id
