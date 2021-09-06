from rest_framework import serializers
from ansibleops.models import Playbook, AnsibleTasks
from vadmin.op_drf.serializers import CustomModelSerializer
from django.conf import settings


class PlaybookSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = Playbook
        fields = '__all__'


class PlaybookSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playbook
        fields = ('id', 'func_name', 'nick_name',)


class PlaybookCreateUpdateSerializer(CustomModelSerializer):
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
        model = Playbook
        fields = '__all__'


class AnsibleTasksSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = AnsibleTasks
        fields = '__all__'


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
