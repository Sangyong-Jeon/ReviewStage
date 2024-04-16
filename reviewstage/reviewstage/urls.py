from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('performance/', include('performance.urls')),
    path('rest/', include('performance_api.urls')),
]
