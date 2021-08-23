from django.shortcuts import render
from prototype.models import User,Questionnaire
import simplejson
from django.http import JsonResponse, HttpResponse, FileResponse
from user_manage.views import get_quizs
# Create your views here.

def info(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        print('params')
        userName = r['userName']
        info = {}
        user = User.objects.get(name=userName)
        info['phone'] = user.phone
        info['mail'] = user.mail
        info['sex'] = user.isMale
        print(info)
        quens = Questionnaire.objects.filter(USER=user,isDeleted=True).order_by('createTime')
        info['quizs'] = get_quizs(quens)

        return JsonResponse({'info': info})

def recover(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        quen = Questionnaire.objects.get(pk=r['ID'])
        quen.isDeleted = False
        quen.save()
        return JsonResponse({'success':True})