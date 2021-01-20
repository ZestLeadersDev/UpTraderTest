from django.contrib import admin, auth
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'dispatcher'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('about/', views.about_view, name='about'),
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='settings'),
]
