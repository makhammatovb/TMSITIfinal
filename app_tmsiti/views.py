from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (AnnouncementsSerializer,
                          NewsSerializer,
                          NewsDetailSerializer,
                          LeadershipSerializer,
                          UnitsSerializer,
                          StandardsSerializer,
                          StandardsInformationSerializer
)
from .models import (Announcements,
                     News,
                     NewsDetail,
                     Leadership,
                     Units,
                     Standards,
                     StandardsInformation,
)
from .permissions import IsSuperuserOrReadOnly
from .filters import (AnnouncementsFilter,
                      NewsFilter,
                      LeadershipFilter,
                      UnitsFilter,
                      StandardsFilter,
)


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


class LeadershipView(viewsets.ModelViewSet):
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = LeadershipFilter


class UnitsView(viewsets.ModelViewSet):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UnitsFilter


class StandardsView(viewsets.ModelViewSet):
    queryset = Standards.objects.all()
    serializer_class = StandardsSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = StandardsFilter


class StandardsInformationView(viewsets.ModelViewSet):
    queryset = StandardsInformation.objects.all()
    serializer_class = StandardsInformationSerializer
    permission_classes = [IsSuperuserOrReadOnly]