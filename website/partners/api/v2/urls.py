"""Partners app API v2 urls."""
from django.urls import path

from partners.api.v2.views import PartnerListView

app_name = "partners"

urlpatterns = [
    path("partners/", PartnerListView.as_view(), name="partners-list"),
]
