from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import (
    SHNKSystemsModel, SHNKGroupsModel, SHNKSubSystemsModel
)

class SHNKSystemModelSerializer(ModelSerializer):

    class Meta:
        model = SHNKSystemsModel
        fields = '__all__'


class SHNKGroupsModelSerializer(ModelSerializer):

    class Meta:
        model = SHNKGroupsModel
        fields = '__all__'


class SHNKSubSystemsModelSerializer(ModelSerializer):

    class Meta:
        model = SHNKSubSystemsModel
        fields = '__all__'