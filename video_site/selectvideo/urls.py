from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'selectvideo'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(next_page='selectvideo:index',
                                                redirect_authenticated_user=True), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('create-user/', views.createUser, name='create_user'),
]
