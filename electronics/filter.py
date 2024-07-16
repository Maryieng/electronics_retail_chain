import django_filters   # type: ignore

from .models import Link


class LinkFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='icontains', label='Страна')

    class Meta:
        model = Link
        fields = ['country']
