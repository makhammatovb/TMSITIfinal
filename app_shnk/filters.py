import django_filters
from django.db.models import Q

from .models import SHNKSystemsModel, SHNKGroupsModel, SHNKSubSystemsModel


class SHNKSystemsFilter(django_filters.FilterSet):
    systems = django_filters.CharFilter(method='systems_filter', label='Search system')

    class Meta:
        model = SHNKSystemsModel
        fields = []

    def systems_filter(self, queryset, name, value):
        try:
            return queryset.filter(Q(system_number=value))
        except:
            return queryset.filter(
                Q(system_name__icontains=value)
            )


class SHNKGroupsFilter(django_filters.FilterSet):
    groups = django_filters.CharFilter(method='groups_filter', label='Search group')

    class Meta:
        model = SHNKGroupsModel
        fields = []

    def groups_filter(self, queryset, name, value):
        try:
            return queryset.filter(Q(group_number=value))
        except:
            return queryset.filter(
                Q(group_name__icontains=value)
            )


class SHNKSubSystemsFilter(django_filters.FilterSet):
    subsystems = django_filters.CharFilter(method='subsystems_filter', label='Search subsystem')

    class Meta:
        model = SHNKSubSystemsModel
        fields = []

    def subsystem_filter(self, queryset, name, value):
        try:
            return queryset.filter(Q(subsystem_code__icontains=value))
        except:
            return queryset.filter(
                Q(subsystem_name__icontains=value)
            )