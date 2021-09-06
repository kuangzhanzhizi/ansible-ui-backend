# from django.conf import settings
from django.db.models import CharField, IntegerField
from vadmin.op_drf.models import CoreModel


class Playbook(CoreModel):
    func_name = CharField(max_length=80, null=True, blank=True)
    nick_name = CharField(max_length=80, null=True, blank=True)
    playbook = CharField(max_length=80, unique=True, null=True, blank=False)
    url = CharField(max_length=80, unique=True, blank=False)

    class Meta:

        verbose_name = '可执行任务（playbook）'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.playbook
