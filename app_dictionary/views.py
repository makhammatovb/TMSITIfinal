from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Dictionary, Word
from .serializers import DictionarySerializer, WordSerializer
from .filters import DictionaryFilter, WordFilter
from .permissions import IsSuperUserOrNot


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [IsSuperUserOrNot]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DictionaryFilter



class WordViewset(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsSuperUserOrNot]
    filter_backends = [DjangoFilterBackend]
    filterset_class = WordFilter