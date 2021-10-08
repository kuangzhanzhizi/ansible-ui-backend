import django_filters

from .models import Host


class HostFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度, 这个=之前的是查询的字段
    conn_ip = django_filters.CharFilter(lookup_expr='icontains')
    # 获取id不等于3，4，5的所有数据
    # models.DjangoInfo.objects.exclude(id__in=[3, 4, 5])

    class Meta:
        model = Host
        # 排除
        exclude = ('description', 'creator', 'modifier')
