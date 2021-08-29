from django.urls import path
from . import views

urlpatterns = [
    path('test1', views.test1, name='test1'),
    path('encode', views.encode, name='encode'),
]