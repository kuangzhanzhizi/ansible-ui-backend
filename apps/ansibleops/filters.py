import django_filters
import json
from .models import AnsibleTasks


class TaskFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    task_user = django_filters.CharFilter(lookup_expr='icontains')
    search_time = django_filters.CharFilter(field_name='create_time', method="filter_create_time")

    def filter_create_time(self, queryset, name, value):
        params = json.loads(self.request.query_params.get('search_time'))
        queryset = AnsibleTasks.objects.filter(create_datetime__range=params["create_datetime__range"])
        return queryset

    class Meta:
        model = AnsibleTasks
        # 排除
        exclude = ('description', 'creator', 'modifier')
