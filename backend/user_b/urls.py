from django.urls import path
from . import views


urlpatterns = [
    path('info', views.info, name='info'),
    path('recover', views.recover, name='recover'),

]