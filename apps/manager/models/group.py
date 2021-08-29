# from django.conf import settings
from django.db.models import CharField, IntegerField
from vadmin.op_drf.models import CoreModel


class Host(CoreModel):
    GROUP_STATUS = (
        (0, '禁用中'),
        (1, '使用中'),
        (2, '暂停中'),
        (3, '不可达'),
    )
    group_name = CharField(max_length=80, null=True, verbose_name='主机组')
    nick_name = CharField(max_length=80, unique=True, verbose_name='别名')
    _status = IntegerField(choices=GROUP_STATUS, default=0)


    class Meta:
        verbose_name = '主机列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.group_name
