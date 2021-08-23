from django.urls import path
from . import views


urlpatterns = [
    path('getQn', views.getQn, name='getQn'),
]