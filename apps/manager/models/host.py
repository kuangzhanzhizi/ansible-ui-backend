# from django.conf import settings
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL, ManyToManyField
from vadmin.op_drf.models import CoreModel


class Host(CoreModel):
    host_name = CharField(max_length=80, null=True, verbose_name='主机名称')
    conn_ip = CharField(max_length=80, unique=True, verbose_name='主机IP')
    ansible_user = CharField(max_length=80, default='root', verbose_name='主机用户')
    ansible_pwd = CharField(max_length=80, blank=True, null=True, verbose_name='密码')
    ssh_key = CharField(max_length=80, default='files/id_rsa',blank=True, null=True, verbose_name='ssh私匙')
    sys_name = CharField(max_length=80, default='Linux', null=True,  verbose_name='系统名称')
    groups = ManyToManyField(to="manager.Group", blank=True, verbose_name=("主机组"))

    class Meta:
        verbose_name = '主机列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.host_name
