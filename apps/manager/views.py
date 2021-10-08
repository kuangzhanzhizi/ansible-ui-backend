from manager.filters import HostFilter
from manager.models import Group, Host
from manager.serializers import HostListSerializer, HostCreateUpdateSerializer, ExportHostSerializer, GroupListSerializer, GroupCreateUpdateSerializer, GroupSerializer
from apps.vadmin.op_drf.filters import DataLevelPermissionsFilter
from apps.vadmin.op_drf.viewsets import CustomModelViewSet
from apps.vadmin.permission.permissions import CommonPermission


class HostModelViewSet(CustomModelViewSet):
    """
    节点管理 的CRUD视图
    """
    queryset = Host.objects.all()
    serializer_class = HostListSerializer  # 序列化器
    create_serializer_class = HostCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = HostCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = HostFilter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('name',)  # 搜索
    ordering = ['create_datetime']  # 默认排序

    # 这四行代码仅仅就是赋值,只有当project/export/, project/importTemplate这两条路由匹配到importTemplate,export的视图集
    # 导出
    export_field_data = ['主机名', 'IP', 'User', '私钥', '主机组', '系统', '创建时间']  # 导出
    export_serializer_class = ExportHostSerializer  # 导出序列化器
    # 导入
    # import_field_data = {'name': '项目名称', 'code': '项目编码', 'person': '项目负责人ID', 'dept': '部门ID'}
    # import_serializer_class = ExportHostSerializer


class GroupModelViewSet(CustomModelViewSet):
    """
    项目管理 的CRUD视图
    """
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer  # 序列化器
    create_serializer_class = GroupCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = GroupCreateUpdateSerializer  # 创建/更新时的列化器
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
    # export_serializer_class = ExportProjectSerializer  # 导出序列化器
    # # 导入
    # import_field_data = {'name': '项目名称', 'code': '项目编码', 'person': '项目负责人ID', 'dept': '部门ID'}
    # import_serializer_class = ExportProjectSerializer
