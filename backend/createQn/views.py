from django.shortcuts import render
from django.http import JsonResponse
import simplejson
from prototype.models import Questionnaire,User
from prototype.base_option import get_questionnaire,questionnaire_create,delete_questionnaire,des_decrypt,des_encrypt

# Create your views here.
def create_or_copy(r):
    que = r['que']
    qnid = que['qnId']
    user = User.objects.get(name=r['userName'])
    que['user'] = user

    if qnid != '0':
        delete_questionnaire({'qnid': des_decrypt(qnid)})
    quen = questionnaire_create(que)
    qnid = des_encrypt(quen.id)
    return qnid

def saveQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print("*********************************r*************************************")
        print(r)
        qnid = create_or_copy(r)
    return JsonResponse({'qnid': qnid})

def copy(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        qnid = des_decrypt(r['qnid'])
        quen = get_questionnaire(qnid)

        dict_r = {}
        dict_r['qnId'] = '0'
        quen_ins = Questionnaire.objects.get(pk=des_decrypt(quen['qnid']))
        dict_r['userName'] = quen_ins.USER.name

        que = {}
        que['title'] = quen['title']
        que['QList'] = quen['QList']
        que['endTime'] = quen['endTime']
        que['qnType'] = quen['qnType']
        que['showNumbers'] = quen_ins.showNumbers
        que['qnId'] = '0'
        dict_r['que'] = que

        print(dict_r)
        qnid= create_or_copy(dict_r)
        quen_copy = Questionnaire.objects.get(pk=des_decrypt(qnid))
        t = quen_copy.title
        quen_copy.title = t+'_copy'
        quen_copy.save()
        return JsonResponse({'qnid': qnid})