from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (AnnouncementsSerializer,
                          NewsSerializer,
                          NewsDetailSerializer)
from .models import Announcements, News, NewsDetail
from .permissions import IsSuperuserOrReadOnly
from .filters import AnnouncementsFilter, NewsFilter


# Create your views here.
class AnnouncementsView(viewsets.ModelViewSet):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnnouncementsFilter


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class NewsDetailView(viewsets.ModelViewSet):
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter
