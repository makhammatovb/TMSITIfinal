from django_filters import CharFilter, FilterSet, NumberFilter
from django.db.models import Q
from django.utils import timezone

from .models import (Announcements,
                     News,
                     NewsDetail,
                     Leadership,
                     Units,
                     Standards
)

class AnnouncementsFilter(FilterSet):
    keyword = CharFilter(method='my_filter', label='Search keyword')

    class Meta:
        model = Announcements
        fields = []

    def my_filter(self, queryset, name, value):
        try:
            start_date, end_date = value.split(',')
            start_date = timezone.make_aware(datetime.datetime.strptime(start_date.strip(), '%Y-%m-%d'))
            end_date = timezone.make_aware(
                datetime.datetime.strptime(end_date.strip(), '%Y-%m-%d')) + timezone.timedelta(days=1)
            return queryset.filter(Q(announcement_date__gte=start_date) &
                                   Q(announcement_date__lt=end_date))
        except:
            return queryset.filter(
                Q(announcement_title__icontains=value) |
                Q(announcement_description__icontains=value)
            )


class NewsFilter(FilterSet):
    keyword = CharFilter(method='keyword_filter', label='Search keyword')

    class Meta:
        model = NewsDetail
        fields = []

    def keyword_filter(self,queryset, name, value):
        try:
            start_date, end_date = value.split(',')
            start_date = timezone.make_aware(datetime.datetime.strptime(start_date.strip(), '%Y-%m-%d'))
            end_date = timezone.make_aware(
                datetime.datetime.strptime(end_date.strip(), '%Y-%m-%d')) + timezone.timedelta(days=1)
            return queryset.filter(
                Q(news_date__gte=start_date) &
                Q(news_date__lt=end_date))
        except:
            return queryset.filter(
                Q(news_title__icontains=value) |
                Q(news_description__icontains=value)
            )


class LeadershipFilter(FilterSet):
    leader = CharFilter(method='leader_filter', label='Search leader')

    class Meta:
        model = Leadership
        fields = []

    def leader_filter(self, queryset, name, value):
        try:
            return queryset.filter(Q(leader_position__icontains=value))
        except:
            return queryset.filter(
                Q(leader_name__icontains=value) |
                Q(leader_days__icontains=value)
            )


class UnitsFilter(FilterSet):
    units = CharFilter(method='units_filter', label='Search staff')

    class Meta:
        model = Units
        fields = []

    def units_filter(self, queryset, name, value):
        try:
            return queryset.filter(Q(staff_position__icontains=value))
        except:
            return queryset.filter(
                Q(staff_name__icontains=value) |
                Q(staff_email__icontains=value)
            )


class StandardsFilter(FilterSet):
    standards = CharFilter(method='standard_filter', label='Search standards')

    class Meta:
        model = Standards
        fields = []

    def standard_filter(self, query, name, value):
        try:
            return self.queryset.filter(Q(standard_name__icontains=value))
        except:
            return self.queryset.filter(
                Q(standard_description__icontains=value)
            )