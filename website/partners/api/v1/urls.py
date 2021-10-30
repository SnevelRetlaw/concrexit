from rest_framework import routers

from . import viewsets

router = routers.SimpleRouter()
router.register(r"partners", viewsets.PartnerViewset)
urlpatterns = router.urls
