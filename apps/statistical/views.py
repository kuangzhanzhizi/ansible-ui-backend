from apps.vadmin.op_drf.filters import DataLevelPermissionsFilter
from apps.vadmin.op_drf.views import CustomAPIView
from apps.vadmin.permission.permissions import CommonPermission
from apps.vadmin.op_drf.response import SuccessResponse, ErrorResponse
from django.contrib.auth import get_user_model
from apps.ansibleops.models.playbook import Playbook
from apps.ansibleops.models.task import AnsibleTasks
from apps.manager.models.host import Host
from apps.manager.models.group import Group


User = get_user_model()


class DashBoardModelViewSet(CustomAPIView):
    """
    dashboard  统计视图
    """
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉

    def get(self, request):
        user_count = User.objects.all().count()
        playbook_count = Playbook.objects.all().count()
        ansible_task_count = AnsibleTasks.objects.all().count()
        host_count = Host.objects.all().count()
        print(host_count)
        group_count = Group.objects.all().count()
        return SuccessResponse(data={
            "user_count": user_count,
            "playbook_count": playbook_count,
            "ansible_task_count": ansible_task_count,
            "host_count": host_count,
            "group_count": group_count
        })
