from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('info', views.info, name='info'),
]