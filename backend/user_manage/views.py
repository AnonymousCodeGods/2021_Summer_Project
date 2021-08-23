from django.shortcuts import render
from prototype.models import User,Questionnaire
import simplejson
from django.http import JsonResponse, HttpResponse, FileResponse
# Create your views here.

def register(request):
    if request.method == 'POST':
        dict = {'success':True}
        r = simplejson.loads(request.body)
        print(r)
        new_username = r['userName']
        new_password = r['pwd']

        test_name = User.objects.filter(name=new_username)

        if test_name.count() != 0:
            dict['success'] = False
            return JsonResponse(dict)

        else:
            new_cus = User()
            new_cus.name = new_username
            new_cus.password = new_password
            new_cus.phone = r['phone']
            new_cus.mail = r['mail']
            new_cus.isMale = r['sex']
            new_cus.save()
            return JsonResponse(dict)

def login(request):
    if request.method == 'POST':
        success = True
        r = simplejson.loads(request.body)
        print(r)
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

def get_quizs(quens):
    quizs = []
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
    return quizs

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
        quens = Questionnaire.objects.filter(USER=user,isDeleted=False).order_by('createTime')
        info['quizs'] = get_quizs(quens)

        return JsonResponse({'info': info})

def search(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        user = User.objects.get(name=r['userName'])
        quens = Questionnaire.objects.filter(USER=user,title__contains=r['key']).order_by('createTime')
        quizs= get_quizs(quens)
        return JsonResponse({'quizs': quizs})

