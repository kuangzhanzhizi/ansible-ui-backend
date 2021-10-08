# from django.conf import settings
import os
import uuid
from django.utils import timezone
from django.db.models import CharField, FileField

from vadmin.op_drf.models import CoreModel


def files_path(instance, filename):
    return '/'.join(['system', 'playbook', filename])


class Playbook(CoreModel):
    func_name = CharField(max_length=80, null=True, blank=True)
    nick_name = CharField(max_length=80, null=True, blank=True)
    playbook = CharField(max_length=80, null=True, blank=False)
    size = CharField(max_length=64, verbose_name="文件大小", null=True, blank=True)
    file = FileField(verbose_name="剧本URL", upload_to=files_path, null=True)

    class Meta:

        verbose_name = '可执行任务（playbook）'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.playbook
