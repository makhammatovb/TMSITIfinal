from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (AnnouncementsSerializer,
                          NewsSerializer,
                          NewsDetailSerializer,
                          LeadershipSerializer,
                          UnitsSerializer,
                          StandardsSerializer,
                          StandardsInformationSerializer,
                          ContactSerializer,
                          BuildingRegulationsSerializer,
)
from .models import (Announcements,
                     News,
                     NewsDetail,
                     Leadership,
                     Units,
                     Standards,
                     StandardsInformation,
                     Contact,
                     BuildingRegulations,
)
from .permissions import IsSuperuserOrReadOnly
from .filters import (AnnouncementsFilter,
                      NewsFilter,
                      LeadershipFilter,
                      UnitsFilter,
                      StandardsFilter,
                      BuildingFilter
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


class ContactsView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class BuildingRegulationsView(viewsets.ModelViewSet):
    queryset = BuildingRegulations.objects.all()
    serializer_class = BuildingRegulationsSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BuildingFilter


@api_view(['GET'])
def full_search(request):
    keyword = request.GET.get('keyword', None)
    if keyword:
        tmsiti_building = list(BuildingRegulationsModel.objects.filter(building_name__icontains=keyword).values_list('id'))
        tmsiti_standards = list(StandardsModel.objects.filter(standard_description__icontains=keyword).values_list('standard_name'))
        tmsiti_date = list(Announcements.objects.filter(announcement_date__icontains=keyword).values_list('announcement_date'))
        tmsiti_news= list(Announcements.objects.filter(news_description__icontains=keyword).values_list('news_name'))

        res = tmsiti_building + tmsiti_standards + tmsiti_news+ tmsiti_date

        result = [0] * len(res)

        for i in range(len(res)):
            result[i] = res[i][0]

        tmsiti_list = Announcements.objects.filter(id__in=set(result))
        serial = AnnouncementsSerializer(tmsiti_list, many=True)

        return Response({'result': serial.data}, status=200)
    else:
        return Response({'message': 'Insert keyword please'}, status=400)
