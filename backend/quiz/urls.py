from django.urls import path
from . import views


urlpatterns = [
    path('submitQn', views.submitQn, name='submitQn'),
    path('result', views.result, name='result'),
    path('publish', views.publish, name='publish'),
    path('suspend', views.suspend, name='suspend'),
    path('clear', views.clear, name='clear'),
    path('recycle', views.recycle, name='recycle'),
    path('recover', views.recover, name='recover'),
]