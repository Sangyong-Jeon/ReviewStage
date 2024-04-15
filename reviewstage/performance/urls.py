from django.urls import path
from . import views

app_name = 'performance'
urlpatterns = [
	path('', views.index, name='index'),
]