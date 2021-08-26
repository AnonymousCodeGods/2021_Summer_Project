from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
import simplejson
from prototype.models import Questionnaire,User,ChoiceQuestion,Complition,Option,Answer,StarNum
import django.utils.timezone as timezone
from prototype.base_option import complition_create,get_questionnaire,choice_create,questionnaire_create,delete_questionnaire,get_options
# Create your views here.
from django.db.models import F
import os

# Create your views here.
def create_or_copy(r):
    que = r['que']
    qnid = r['qnid']
    user = User.objects.get(name=r['userName'])
    que['user'] = user
    if qnid != 0:
        delete_questionnaire({'qnid': qnid})
    quen = questionnaire_create(que)
    print('quen')
    print(quen.id)
    qnid = quen.id
    return qnid

def saveQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        qnid = create_or_copy(r)
    return JsonResponse({'qnid': qnid})

def copy(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        qnid = r['qnid']
        quen = get_questionnaire(qnid)
        print(quen)

        dict_r = {}
        dict_r['qnid'] = 0
        quen_ins = Questionnaire.objects.get(pk=quen['qnid'])
        dict_r['userName'] = quen_ins.USER.name

        que = {}
        que['title'] = quen['title']
        que['QList'] = quen['QList']
        dict_r['que'] = que

        qnid= create_or_copy(dict_r)
        return JsonResponse({'qnid': qnid})