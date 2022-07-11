from django.urls import path
from . import views

app_name = 'playback'
urlpatterns = [
    path('', views.index, name='index'),
]
