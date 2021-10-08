from ansibleops.models import Playbook, AnsibleTasks
from vadmin.op_drf.serializers import CustomModelSerializer

from rest_framework import serializers


class PlaybookSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """
    file_url = serializers.CharField(read_only=True, source='file.url')

    class Meta:
        model = Playbook
        fields = '__all__'


class PlaybookSelectSerializer(CustomModelSerializer):

    class Meta:
        model = Playbook
        fields = ('id', 'func_name', 'nick_name',)


class PlaybookCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """
    file_url = serializers.SerializerMethodField(read_only=True)

    def get_file_url(self, obj: Playbook):
        return getattr(obj.file, "url", obj.file) if hasattr(obj, "file") else ""

    def save(self, **kwargs):
        files = self.context.get('request').FILES.get('file')
        if files:
            self.validated_data['playbook'] = files.name
            self.validated_data['size'] = files.size
            instance = super().save(**kwargs)
            # 进行判断是否需要OSS上传
            return instance
        return super().save(**kwargs)

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)


    class Meta:
        model = Playbook
        fields = '__all__'


class AnsibleTasksSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = AnsibleTasks
        fields = '__all__'

    # def validate_create_datetime(self, value):
    #     raise ValueError("hello world")


class AnsibleTasksCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    def create(self, validated_data):
        pass
        # print(settings.ALLOWED_HOSTS)
        # self.validated_data['url'] = self.initial_data.get('url', None)

    class Meta:
        model = AnsibleTasks
        fields = '__all__'
