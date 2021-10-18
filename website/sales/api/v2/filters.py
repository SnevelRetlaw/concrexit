from django_filters import rest_framework as filters

from sales.models.shift import Shift


class ShiftFilter(filters.FilterSet):
    start = filters.DateTimeFilter(field_name="start", lookup_expr="gte")
    end = filters.DateTimeFilter(field_name="end", lookup_expr="lte")
    active = filters.BooleanFilter(field_name="active", method="filter_active")

    def filter_active(self, queryset, name, value):
        return queryset.filter(active=value)

    class Meta:
        model = Shift
        fields = ["locked"]
