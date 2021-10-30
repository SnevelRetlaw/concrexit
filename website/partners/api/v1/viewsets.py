from rest_framework import viewsets

from partners.models import Partner
from .serializers import PartnerSerializer


class PartnerViewset(viewsets.ReadOnlyModelViewSet):
    """View set for partners."""

    serializer_class = PartnerSerializer
    queryset = Partner.objects.filter(is_active=True)
