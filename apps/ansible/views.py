# from manager.filters import ProjectFilter
from ansible.models import Playbook
from ansible.serializers import PlaybookSerializer, PlaybookCreateUpdateSerializer, PlaybookSelectSerializer
from apps.vadmin.op_drf.filters import DataLevelPermissionsFilter
from apps.vadmin.op_drf.viewsets import CustomModelViewSet
from apps.vadmin.permission.permissions import CommonPermission
from apps.vadmin.op_drf.response import SuccessResponse, ErrorResponse

from rest_framework.request import Request


class PlaybookViewSet(CustomModelViewSet):
    """
    节点管理 的CRUD视图
    """
    queryset = Playbook.objects.all()
    serializer_class = PlaybookSerializer  # 序列化器
    create_serializer_class = PlaybookCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = PlaybookCreateUpdateSerializer  # 创建/更新时的列化器
    # filter_class = ProjectFilter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('name',)  # 搜索
    ordering = ['create_datetime']  # 默认排序

    # 这四行代码仅仅就是赋值,只有当project/export/, project/importTemplate这两条路由匹配到importTemplate,export的视图集
    # 导出
    # export_field_data = ['项目序号', '项目名称', '项目编码', '项目负责人', '项目所属部门', '创建者', '修改者', '备注']  # 导出
    # export_serializer_class = ExportHostSerializer  # 导出序列化器
    # 导入
    # import_field_data = {'name': '项目名称', 'code': '项目编码', 'person': '项目负责人ID', 'dept': '部门ID'}
    # import_serializer_class = ExportHostSerializer

    def playbook_select(self, request: Request, *args, **kwargs):
        """
            GeneriacAPIView中
            self.get_query 获得所有的对象 == APIView中的model.object.all()
            self.get_serializer 获得序列化器
            self.get_get_object 获取的是单一数据对象
        """
        queryset = self.filter_queryset(self.get_queryset())
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        serializer = PlaybookSelectSerializer(queryset, many=True)
        try:
            pb = self.get_object()
            with open('playbooks/%s' % pb) as f:
                s = f.read()
        except:
            return ErrorResponse()
        for data in serializer.data:
            data["content"] = '```yaml\n%s\n```' % s
        return SuccessResponse(serializer.data)
