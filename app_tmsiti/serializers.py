from rest_framework import serializers

from .models import (Announcements,
                     News,
                     NewsDetail,
                     Leadership,
                     Units,
                     Standards,
                     StandardsInformation
)


class AnnouncementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcements
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'


class NewsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsDetail
        fields = '__all__'


class LeadershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leadership
        fields = '__all__'


class UnitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Units
        fields = '__all__'


class StandardsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Standards
        fields = '__all__'


class StandardsInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StandardsInformation
        fields = '__all__'