# from django.conf import settings
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL
from vadmin.op_drf.models import CoreModel


class NodeLists(CoreModel):
    hostname = CharField(max_length=20, null=True, verbose_name='节点名称')
    ip = CharField(max_length=80, unique=True)
    ansible_user = CharField(max_length=80, default='root')
    ansible_pass = CharField(max_length=80, blank=True, null=True, )
    ansilbe_key = CharField(max_length=80, default='files/id_rsa')

    class Meta:
        verbose_name = '主机列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hostname
