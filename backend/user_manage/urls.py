from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('info', views.info, name='info'),
    path('search', views.search, name='search'),
    path('set_end', views.set_endTime, name='set_end'),
]