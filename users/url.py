from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projects/<slug:practice_area_slug>/', views.projects, name='projects'),
    path('input/', views.user_input, name='input'),
]