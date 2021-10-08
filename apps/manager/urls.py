from django.urls import re_path
from rest_framework.routers import DefaultRouter

from manager.views import HostModelViewSet, GroupModelViewSet

router = DefaultRouter()
router.register(r'manager/host', HostModelViewSet)
# router.register(r'manager/host', HostModelViewSet)
router.register(r'manager/group', GroupModelViewSet)

urlpatterns = [
    # 导出项目
    re_path('manager/export/', HostModelViewSet.as_view({'get': 'export', })),
    # 项目导入模板下载及导入
    # re_path('project/importTemplate/',
    #         ProjectModelViewSet.as_view({'get': 'importTemplate', 'post': 'importTemplate'})),
]

urlpatterns += router.urls
