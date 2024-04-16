from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('performances', PerformanceViewSet)
router.register('reviews', ReviewViewSet)
router.register('files', FileViewSet)

urlpatterns = router.urls