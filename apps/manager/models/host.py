# from django.conf import settings
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL
from vadmin.op_drf.models import CoreModel


class Host(CoreModel):
    host_name = CharField(max_length=80, null=True, verbose_name='节点名称')
    conn_ip = CharField(max_length=80, unique=True, verbose_name='节点IP')
    ansible_user = CharField(max_length=80, default='root', verbose_name='节点用户')
    ansible_pass = CharField(max_length=80, blank=True, null=True, verbose_name='密码')
    ansilbe_key = CharField(max_length=80, default='files/id_rsa', verbose_name='ssh私匙')
    sys_name = CharField(max_length=80, default='files/id_rsa', verbose_name='系统名称')


    class Meta:
        verbose_name = '主机列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hostname
