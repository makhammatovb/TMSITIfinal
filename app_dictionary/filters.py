import django_filters
from django.db.models import Q

from .models import Dictionary, Word

class DictionaryFilter(django_filters.FilterSet):
    dict = django_filters.CharFilter(method='dictionary_filter', label='Search word')

    class Meta:
        model = Dictionary
        fields = []

    def dictionary_filter(self, queryset, name, value):
        try:
            return queryset.filter(Q(word_uz__icontains=value))
        except:
            return queryset.filter(
                Q(word_ru__icontains=value) |
                Q(word_en__icontains=value) |
                Q(word_tk__icontains=value)
            )


class WordFilter(django_filters.FilterSet):
    word = django_filters.CharFilter(method='word_filter', label='Search word description')

    class Meta:
        model = Word
        fields = []

    def word_filter(self, queryset, name, value):
        try:
            return queryset.filter(Q(word_description_uz__icontains=value))
        except:
            return queryset.filter(
                Q(word_description_ru__icontains=value) |
                Q(word_description_en__icontains=value) |
                Q(word_description_tk__icontains=value)
            )