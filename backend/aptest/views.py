from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
import simplejson
from prototype.models import Questionnaire,User,ChoiceQuestion,Complition,Option,CMPAnswer,StarNum
import django.utils.timezone as timezone
from prototype.base_option import complition_create,get_questionnaire,choice_create,questionnaire_create,delete_questionnaire,get_options,get_ques_ins,get_op_ins
# Create your views here.
from django.db.models import F
import os
import base64
from prototype.base_option import des_decrypt,des_encrypt
def test1(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        qins = get_ques_ins(r['qnid'])
        ops = get_op_ins(qins[0])
        print(qins)
        print(ops)
        return JsonResponse({})

def encode(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        s = des_encrypt(r['qnid'])
        print(des_decrypt(s))
        return JsonResponse({'code':s})






