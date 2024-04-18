from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'performance'
urlpatterns = [
	path('', RedirectView.as_view(url='login/')),
	path('login/', views.CustomLoginView.as_view(), name='login'),
	path('signup/', views.SignupView.as_view(), name='signup'),
	path('main/', views.index, name='index'),
]