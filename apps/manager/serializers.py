
from rest_framework import serializers
from manager.models import Host, Group
from vadmin.op_drf.serializers import CustomModelSerializer


class GroupSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = Group
        fields = ('group_name', 'nick_name')


class HostListSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """
    groups = GroupSerializer(many=True)

    class Meta:
        model = Host
        fields = '__all__'


class GroupListSerializer(CustomModelSerializer):
    hosts = HostListSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'


class GroupCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Group
        fields = '__all__'


class HostCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Host
        fields = '__all__'


class ExportHostSerializer(CustomModelSerializer):
    """
    导出 项目管理 简单序列化器
    """

    class Meta:
        model = Host
        fields = '__all__'

