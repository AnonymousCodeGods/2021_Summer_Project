from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
import simplejson
from prototype.models import Questionnaire,User,ChoiceQuestion,Complition,Option,Answer,StarNum
import django.utils.timezone as timezone
from prototype.base_option import complition_create,get_questionnaire,choice_create,questionnaire_create,delete_questionnaire,get_options
# Create your views here.
from django.db.models import F
import os

def test1(request):
    if request.method == 'POST':
        print("s")
        path = os.path.dirname(__file__)

        r = simplejson.loads(request.body)
        userType = r['type']
        os.system("python D:\max\软工小学期\\backend\\amazing-qr-master\\amazing-qr-master\\amzqr.py https://baidu.com")
        #if userType in ['管理员','调度员']:
    return JsonResponse({"user":userType,"pic":'D:\max\软工小学期\\backend\qrcode.png'})

def test2(request):
    if request.method == 'POST':
        print("s1")
        file = open('D:\max\软工小学期\\backend\extest.xlsx', 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="extest.xlsx"'
        print(response)
        return response

def test3(request):
    if request.method == 'POST':
        print("s3")
        q = Questionnaire.objects.create(type=1,publishTime=timezone.now())
        u = User.objects.create(name='ling1',password='235')
        userType = 'u'
        return JsonResponse({"user": userType})

def test4(request):
    if request.method == 'POST':
        dict = {'content': 'r', 'quesNum': 1,'LQID':'CMP23'}
        #dict = {'content': 'r', 'quesNum': 1}
        print(dict)
        complition_create(dict)
        userType = 'u'
        return JsonResponse({"user": userType})

def test5(request):
    if request.method == 'POST':
        #dict = {'content': 'r', 'quesNum': 1,'options':[{'content':'A1'},{'content':'B2'}],'isMulti':True}
        dict = {'content': 'r', 'quesNum': 1,'options':[],'isMulti':None}
        print(dict)
        choice_create(dict)
        userType = 'u'
        return JsonResponse({"user": userType})

def test6(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        que = r['que']
        que['share'] = r['share']
        questionnaire_create(que)
        return JsonResponse({"success": True})

def getQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        QnId = r['QnId']
        que = get_questionnaire(QnId)
        return JsonResponse({'que':que})

def delQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        QnId = r['qnid']
        s =delete_questionnaire(r)
        return JsonResponse({'success':s})

def get_q(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        return JsonResponse({'success':True})

def submitQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        AnswerList = r['AnswerList']
        for ans in AnswerList:
            qid = ans['qid']
            type = ans['type']
            answer = ans['answer']
            choi = None
            if type in [0,1,3]:
                choi = ChoiceQuestion.objects.get(pk=qid)
                options = get_options(choi)
                print(options)
                p = choi.participantsNum
                choi.participantsNum = p+1
                choi.save()
            if type == 0:
                opi = options[answer]
                sNum = opi.selectedNum
                opi.selectedNum = sNum+1
                opi.save()
            elif type == 1:
                for a in answer:
                    opi = options[a]
                    sNum = opi.selectedNum
                    opi.selectedNum = sNum + 1
                    opi.save()
                    pass
            elif type == 2:
                comp = Complition.objects.get(pk=qid)
                p = comp.participantsNum
                comp.participantsNum = p+1
                comp.save()
                ans_ins = Answer(content=answer,CMP=comp)
                ans_ins.save()
            elif type == 3:
                try:
                    starNum = StarNum.objects.get(CH=choi)
                except :
                    starNum = StarNum(CH=choi)
                    starNum.save()
                if answer == 0:
                    sum = starNum.zero_star
                    starNum.zero_star = sum + 1
                elif answer == 1:
                    sum = starNum.one_star
                    starNum.one_star = sum + 1
                elif answer == 2:
                    sum = starNum.two_star
                    starNum.two_star = sum + 1
                elif answer == 3:
                    sum = starNum.three_star
                    starNum.three_star = sum + 1
                elif answer == 4:
                    sum = starNum.four_star
                    starNum.four_star = sum + 1
                elif answer == 5:
                    sum = starNum.five_star
                    starNum.five_star = sum + 1
                starNum.save()
                pass
            pass
        return JsonResponse({'success':True})