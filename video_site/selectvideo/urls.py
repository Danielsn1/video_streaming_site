from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse
from . import views

app_name = 'selectvideo'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(next_page='index'), name='login'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('create-user/', views.createUser, name='create_user'),
]
