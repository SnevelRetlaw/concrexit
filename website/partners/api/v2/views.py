from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope
from rest_framework import filters as framework_filters
from rest_framework.generics import ListAPIView

from partners.api.v2.serializers.partner import PartnerSerializer
from partners.models import Partner


class PartnerListView(ListAPIView):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.filter(is_active=True)
    filter_backends = (
        framework_filters.OrderingFilter,
        framework_filters.SearchFilter,
    )
    ordering_fields = ("name", "pk")
    search_fields = ("name",)
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ["partners:read"]
