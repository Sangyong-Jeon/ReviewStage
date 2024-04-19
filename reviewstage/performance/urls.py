from django.urls import path
from .views import HomeView

from django.views.generic import RedirectView
from . import views

app_name = 'performance'
urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('home/', HomeView.as_view(), name='index'),
]
