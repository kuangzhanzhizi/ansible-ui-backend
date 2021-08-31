from django.urls import re_path
from rest_framework.routers import DefaultRouter

from ansible.views import PlaybookViewSet

router = DefaultRouter()
router.register(r'ansible/playbook', PlaybookViewSet)

urlpatterns = [
    # 导出项目
    # re_path('project/export/', ProjectModelViewSet.as_view({'get': 'export', })),
    # 项目导入模板下载及导入
    # re_path('project/importTemplate/',
    #         ProjectModelViewSet.as_view({'get': 'importTemplate', 'post': 'importTemplate'})),
    # 根据playbook查看
    re_path('playbook/detail/(?P<pk>.*)/', PlaybookViewSet.as_view({'get': 'playbook_select'})),
]

urlpatterns += router.urls
