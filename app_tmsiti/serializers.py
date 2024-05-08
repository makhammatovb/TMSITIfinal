from rest_framework import serializers

from .models import Announcements, News, NewsDetail


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