from .models.node import NodeLists
from vadmin.op_drf.serializers import CustomModelSerializer


class NodeListSerializer(CustomModelSerializer):
    """
    节点列表 简单序列化器
    """
    class Meta:
        model = NodeLists
        fields = '__all__'


class NodeListCreateUpdateSerializer(CustomModelSerializer):
    """
    节点列表 创建/更新时序列化器
    """
    def validate(self, attrs:dict):
        return super().validate(attrs)

    class Meta:
        model = NodeLists
        fields = '__all__'


class ExportNodeListSerializer(CustomModelSerializer):
    """
    导出 节点列表 简单序列化器
    """
    class Meta:
        model = NodeLists
        fields = ('id', 'hostname', 'ip', 'ansible_user', 'ansible_pass', 'ansilbe_key', 'creator', 'modifier',
                  'description')
