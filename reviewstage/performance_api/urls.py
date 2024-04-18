from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()
router.register('performances', PerformanceViewSet)
router.register('reviews', ReviewViewSet)
router.register('files', FileViewSet)

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('register/', RegisterUser.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('files/visual/', get_visual_file, name='visual'),
    *router.urls,
]
