from django.urls import path
from . import views

urlpatterns = [
    path('saveQn', views.saveQn, name='saveQn'),
    path('copy', views.copy, name='copy'),
]