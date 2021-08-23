from django.urls import path
from . import views


urlpatterns = [
    path('submitQn', views.submitQn, name='submitQn'),
    path('result', views.result, name='result'),
    path('publish', views.publish, name='publish'),
    path('suspend', views.suspend, name='suspend'),
]