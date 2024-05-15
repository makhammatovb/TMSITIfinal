from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    SHNKSystemsModel,
    SHNKGroupsModel,
    SHNKSubSystemsModel
)
from .serializers import (
    SHNKSystemModelSerializer,
    SHNKGroupsModelSerializer,
    SHNKSubSystemsModelSerializer
)
from .filters import (
    SHNKSystemsFilter,
    SHNKSubSystemsFilter,
    SHNKGroupsFilter
)
from .permissions import (IsSuperOrReadOnly)


class SHNKSystemModelViewSet(ModelViewSet):
    queryset = SHNKSystemsModel.objects.all()
    serializer_class = SHNKSystemModelSerializer
    permission_classes = [IsSuperOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SHNKSystemsFilter


class SHNKGroupsModelViewSet(ModelViewSet):
    queryset = SHNKGroupsModel.objects.all()
    serializer_class = SHNKGroupsModelSerializer
    permission_classes = [IsSuperOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SHNKGroupsFilter


class SHNKSubSystemsModelViewSet(ModelViewSet):
    queryset = SHNKSubSystemsModel.objects.all()
    serializer_class = SHNKSubSystemsModelSerializer
    permission_classes = [IsSuperOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SHNKSubSystemsFilter