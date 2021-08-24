from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
import simplejson
from prototype.models import Questionnaire,User,ChoiceQuestion,Complition,Option,Answer,StarNum
import django.utils.timezone as timezone
from prototype.base_option import complition_create,get_questionnaire,choice_create,questionnaire_create,delete_questionnaire,get_options
# Create your views here.
import django.utils.timezone
from django.db.models import F
import os
import datetime
from collections import Counter
# Create your views here.



def submitQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print("****************************************************************")
        print(r)
        quen = get_questionnaire(r['qnid'])
        print(quen)
        QList = quen['QList']
        i = 0
        AnswerList = r['AnswerList']
        for ans in AnswerList:
            qid = QList[i]['qid']
            i = i+1
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
        qnid = r['qnid']
        qn = Questionnaire.objects.get(pk=qnid)
        re = qn.recoverNum
        qn.recoverNum = re+1
        qn.save()
        return JsonResponse({'success':True})

def result(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        resultList = {}
        AnswerList = []
        qnid = r['ID']
        quen = get_questionnaire(qnid)
        QList = quen['QList']
        for q in QList:
            Answeri = {}
            Answeri['type'] = q['type']
            qid = q['qid']
            Answeri['Qnum'] = qid
            selection = None
            if q['type'] in [0,1,3]:
                selection = []
                if q['type'] != 3:
                    options = q['option']
                    for option in options:
                        op = Option.objects.get(id=option['oid'])
                        selection.append(op.selectedNum)

                else:
                    star = StarNum.objects.get(CH=qid)
                    selection.append(star.zero_star)
                    selection.append(star.one_star)
                    selection.append(star.two_star)
                    selection.append(star.three_star)
                    selection.append(star.four_star)
                    selection.append(star.five_star)
                Answeri['selection'] = selection
            else:
                input = []
                comp = Complition.objects.get(pk=qid)
                answers = Answer.objects.filter(CMP=comp)
                for answer in answers:
                    input.append(answer.content)

                Answeri['input'] = input
            AnswerList.append(Answeri)
        return JsonResponse({'AnswerList':AnswerList})

def publish(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = Questionnaire.objects.get(id=r['ID'])
        quen.isPublished = True
        quen.publishTime = django.utils.timezone.now()+datetime.timedelta(hours=8)
        quen.save()
    return JsonResponse({'success':True})

def recycle(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = Questionnaire.objects.get(id=r['ID'])
        quen.isDeleted = True

        quen.save()
        print(quen.isDeleted)
    return JsonResponse({'success': True})

def recover(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = Questionnaire.objects.get(id=r['ID'])
        quen.isDeleted = False
        quen.save()
        print(quen.isDeleted)
    return JsonResponse({'success': True})

def suspend(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = Questionnaire.objects.get(id=r['ID'])
        quen.isPublished = False
        quen.save()
        print(quen.isDeleted)
    return JsonResponse({'success': True})

def clear(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = get_questionnaire(r['qnid'])
        quen_ins = Questionnaire.objects.get(pk=r['qnid'])
        quen_ins.recoverNum = 0
        quen_ins.save()
        print(quen)
        QList = quen['QList']
        for q in QList:
            type = q['type']
            if type in[0,1,3]:
                choi = ChoiceQuestion.objects.get(id=q['qid'])
                choi.participantsNum = 0
                choi.save()
                if type != 3:
                    option = q['option']
                    for opt in option:
                        op = Option.objects.get(pk=opt['oid'])
                        op.selectedNum = 0
                        op.save()
                else:
                    star = StarNum.objects.get(CH=choi)
                    star.zero_star = 0
                    star.one_star = 0
                    star.two_star = 0
                    star.three_star = 0
                    star.four_star = 0
                    star.five_star = 0
                    star.save()
                    pass
                pass
            else:
                comp = Complition.objects.get(pk=q['qid'])
                Answer.objects.filter(CMP=comp).delete()
                comp.participantsNum = 0
                comp.save()
    return JsonResponse({'success': True})