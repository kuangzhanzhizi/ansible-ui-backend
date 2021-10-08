from django.urls import re_path
from rest_framework.routers import DefaultRouter

from statistical.views import DashBoardModelViewSet

router = DefaultRouter()
# router.register(r'project', ProjectModelViewSet)

urlpatterns = [
    # 主页数据统计
    re_path('statistical/dashboard/', DashBoardModelViewSet.as_view()),
]

urlpatterns += router.urls
