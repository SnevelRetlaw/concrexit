from html import unescape

from django.utils.html import strip_tags
from rest_framework import serializers

from partners.models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    """Partner serializer."""

    class Meta:
        """Meta class for partner serializer."""

        model = Partner
        fields = (
            "pk",
            "name",
            "link",
            "company_profile",
            "address",
            "zip_code",
            "city",
            "logo",
        )
