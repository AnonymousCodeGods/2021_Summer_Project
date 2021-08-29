from django.urls import path
from . import views


urlpatterns = [
    path('submitQn', views.submitQn, name='submitQn'),
    path('subTest', views.subTest, name='subTest'),
    path('result', views.result, name='result'),
    path('publish', views.publish, name='publish'),
    path('suspend', views.suspend, name='suspend'),
    path('clear', views.clear, name='clear'),
    path('recycle', views.recycle, name='recycle'),
    path('recover', views.recover, name='recover'),
    path('idp_result', views.independent_result, name='idp_recover'),
    path('submitSignUpQn', views.submitSignUpQn, name='submitSignUpQn'),
    path('refresh', views.refresh, name='refresh'),
    path('score_stat', views.score_stat, name='score_stat'),
]