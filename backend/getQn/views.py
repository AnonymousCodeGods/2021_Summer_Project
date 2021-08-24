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
# Create your views here.
def getQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        QnId = r['QnId']
        print(QnId)
        que = get_questionnaire(QnId)
        return JsonResponse({'que':que})
    if request.method == 'GET':
        r = simplejson.loads(request.body)
        print(r)
        QnId = r['QnId']
        print(QnId)
        que = get_questionnaire(QnId)
        return JsonResponse({'que':que})