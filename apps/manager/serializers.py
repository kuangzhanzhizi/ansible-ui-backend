
from rest_framework import serializers
from manager.models import Host, Group
from vadmin.op_drf.serializers import CustomModelSerializer


class GroupSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = Group
        fields = ('group_name', 'nick_name', 'id')


class HostListSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """
    groups = GroupSerializer(many=True)

    class Meta:
        model = Host
        fields = '__all__'


class HostSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = Host
        exclude = ('groups', 'update_datetime', 'modifier', 'description', 'dept_belong_id', 'creator')


class GroupListSerializer(CustomModelSerializer):

    hosts = HostSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'


class GroupCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    def create(self, validated_data):
        hosts = getattr(self.request, 'hosts', None)
        return super().create(validated_data)


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

