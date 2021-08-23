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
        qnid = r['qnid']
        qn = Questionnaire.objects.get(pk=qnid)
        re = qn.recoverNum
        qn.recoverNum = re+1
        qn.save()
        return JsonResponse({'success':True})