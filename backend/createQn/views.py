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





def saveQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        que = r['que']
        qnid = r['qnid']
        user = User.objects.get(name=r['userName'])
        que['user'] = user
        if qnid != 0:
            delete_questionnaire({'qnid':qnid})
        quen = questionnaire_create(que)
        print('quen')
        print(quen.id)
        qnid = quen.id

    return JsonResponse({'qnid': qnid})