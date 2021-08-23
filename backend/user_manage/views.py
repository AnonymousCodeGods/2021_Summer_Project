from django.shortcuts import render
from prototype.models import User,Questionnaire
import simplejson
from django.http import JsonResponse, HttpResponse, FileResponse
# Create your views here.
def login(request):
    if request.method == 'POST':
        success = True
        r = simplejson.loads(request.body)
        userName = r['userName']
        pwd = r['pwd']
        try:
            user = User.objects.get(name=userName)
        except:
            success = False
        if success:
            if user.password != pwd:
                success = False
    return JsonResponse({'success':success})

def info(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        userName = r['userName']
        info = {}
        user = User.objects.get(name=userName)
        info['phone'] = user.phone
        info['mail'] = user.mail
        info['sex'] = user.isMale
        print(info)
        quizs = []
        quens = Questionnaire.objects.filter(USER=user).order_by('createTime')
        for quen in quens:
            quiz = {}
            quiz['name'] = quen.title
            quiz['ID'] = quen.id
            quiz['state'] = quen.isPublished
            quiz['createDate'] = quen.createTime
            quiz['pubDate'] = quen.publishTime
            quiz['bin'] = quen.isDeleted
            quiz['num'] = quen.recoverNum
            quizs.append(quiz)
        info['quizs'] = quizs

        return JsonResponse({'info': info})