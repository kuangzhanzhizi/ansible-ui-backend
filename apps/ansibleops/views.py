from ansibleops.filters import TaskFilter
from ansibleops.models import Playbook, AnsibleTasks
from ansibleops.serializers import PlaybookSerializer, PlaybookCreateUpdateSerializer, PlaybookSelectSerializer, AnsibleTasksSerializer, AnsibleTasksCreateUpdateSerializer
from application.celery_tasks.ansible_task.task import ansible_playbook_api_29
from apps.vadmin.op_drf.filters import DataLevelPermissionsFilter
from apps.vadmin.op_drf.viewsets import CustomModelViewSet
from apps.vadmin.permission.permissions import CommonPermission
from apps.vadmin.op_drf.response import SuccessResponse, ErrorResponse
from apps.vadmin.utils.file_util import get_all_files, remove_empty_dir, delete_files


import os
import datetime
import random
import string
import json
from rest_framework.request import Request
from django.conf import settings


class PlaybookViewSet(CustomModelViewSet):
    """
    playbook 的CRUD视图
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
        pk = kwargs.get("pk")
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(id=pk).order_by("create_datetime")
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        serializer = PlaybookSelectSerializer(queryset, many=True)
        try:
            pb = self.get_object()
            print(pb)
            with open('media/system/playbook/%s' % pb) as f:
                s = f.read()
        except:
            return ErrorResponse()
        for data in serializer.data:
            data["content"] = '\n%s\n' % s
        return SuccessResponse(serializer.data)

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return SuccessResponse(serializer.data, status=201, headers=headers)

    def clear_playbook(self, request: Request, *args, **kwargs):
        """
        清理废弃剧本
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 获取废弃文件列表
        file_list = get_all_files(os.path.join(settings.MEDIA_ROOT, 'system/playbook'))
        queryset_files = [os.path.join(os.path.join(settings.MEDIA_ROOT) + os.sep, ele) for ele in list(self.get_queryset().values_list('file', flat=True))]
        queryset_files_dir = set(map(lambda absdir: os.path.abspath(absdir), queryset_files))
        delete_list = list(set(file_list) - queryset_files_dir)
        # 进行文件删除操作
        delete_files(delete_list)
        # 递归删除空文件
        remove_empty_dir(os.path.join(settings.MEDIA_ROOT, 'system'))
        return SuccessResponse(msg=f"成功清理废弃文件{len(delete_list)}个")


class AnsibleTasksViewSet(CustomModelViewSet):
    queryset = AnsibleTasks.objects.all()
    serializer_class = AnsibleTasksSerializer
    create_serializer_class = AnsibleTasksCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = AnsibleTasksCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = TaskFilter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('name',)  # 搜索
    ordering = ['create_datetime']  # 默认排序

    # def get_queryset(self):
    #     # 重写get_quertset方法 根据前端传递的keyword查询不同的数据 获取keyword数据
    #     create_datatime = self.request.query_params.get('search_time')  # self保存的有request对象
    #     if create_datatime:
    #         res = AnsibleTasks.objects.filter(create_datetime__range=("2021-09-14","2021-09-16"))
    #         return res
    #     else:
    #         return super().get_queryset()

    def ansible_task_create(self, request: Request, *args, **kwargs):
        """
            创建ansible任务
        """
        # 我们需要在 django的 视图函数 中对 request 中的数据进行一定的修改，然后才将数据传到 serializer中去
        # https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.QueryDict.copy
        data = request.data.copy()
        exec_ip = self.request.data.get("conn_ip", None)
        group_name = self.request.data.get("groups", None)
        print(group_name)
        playbook_id = self.request.data.get('playbookId')
        if playbook_id:
            playbook = str(Playbook.objects.filter(id=playbook_id)[0])
        extra_vars = self.request.data.get('extraVars', {}) or {}
        if not extra_vars.get('group_name'):
            extra_vars['group_name'] = group_name
        tid = "AnsibleApiPlaybook-drf-%s-%s" % (''.join(random.sample(string.ascii_letters + string.digits, 8)),
                                                datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        print('添加新的drf playbook 任务：%s: %s: %s' % (tid, playbook, extra_vars))
        celery_task = ansible_playbook_api_29.apply_async((tid, playbook, extra_vars, exec_ip))
        data.update({'ansible_id': tid, 'celery_id': celery_task.task_id, 'group_name': group_name,
                     'extra_vars': json.dumps(extra_vars), 'label': request.META.get('REMOTE_ADDR')})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # 保存
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return SuccessResponse(serializer.data, headers=headers)


