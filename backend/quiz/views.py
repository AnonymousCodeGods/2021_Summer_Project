from django.shortcuts import render
from django.http import JsonResponse
import simplejson
from prototype.models import Questionnaire,ChoiceQuestion,Complition,Option,CMPAnswer,StarNum,LocationQuestion,LOAnswer,User,CHAnswer,FillRecord
from prototype.base_option import complition_create,get_questionnaire,choice_create,questionnaire_create,delete_questionnaire,get_options,get_ques_ins,des_decrypt,des_encrypt
# Create your views here.
import django.utils.timezone
import datetime

# Create your views here.
from .submit_option import ordi_submit,sign_submit

def refresh(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        encodeId = r['qnid']
        quen = Questionnaire.objects.get(code=encodeId)
        quen.key =r['key']
        quen.save()
        newId = des_encrypt(quen.pk)
    return JsonResponse({'newId':newId})

def subTest(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        ordi_submit(r)
    return JsonResponse({'success':True})

def submitQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        flag = ordi_submit(r)
        return JsonResponse({'success':flag})

def submitSignUpQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        condition = sign_submit(r)
    return JsonResponse({'success':condition['success'],'msg':condition['msg']})

def result(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        resultList = {}
        AnswerList = []
        qnid = des_decrypt(r['ID'])
        quen = get_questionnaire(qnid)
        QList = quen['QList']
        for q in QList:
            Answeri = {}
            Answeri['type'] = q['type']
            Answeri['title'] = q['title']

            qid = q['qid']
            Answeri['Qnum'] = qid
            selection = None
            if q['type'] in [0,1,3]:
                selection = []
                op_title = []
                if q['type'] != 3:
                    options = q['option']
                    for option in options:
                        op = Option.objects.get(id=option['oid'])
                        selection.append(op.selectedNum)
                        op_title.append(op.content)

                else:
                    star = StarNum.objects.get(CH=qid)
                    selection.append(star.zero_star)
                    selection.append(star.one_star)
                    selection.append(star.two_star)
                    selection.append(star.three_star)
                    selection.append(star.four_star)
                    selection.append(star.five_star)
                Answeri['selection'] = selection
                Answeri['option'] = op_title
            elif q['type'] == 2:
                input = []
                comp = Complition.objects.get(pk=qid)
                answers = CMPAnswer.objects.filter(CMP=comp)
                for answer in answers:
                    input.append(answer.content)
            elif q['type'] == 4:
                input = []
                loc = LocationQuestion.objects.get(pk=qid)
                answers = LOAnswer.objects.filter(LO=loc)
                for answer in answers:
                    input.append(answer.content)

                Answeri['input'] = input
            AnswerList.append(Answeri)
        quen_ins = Questionnaire.objects.get(pk=qnid)

        return JsonResponse({'totalNum':quen_ins.recoverNum,'AnswerList':AnswerList})

def publish(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = Questionnaire.objects.get(id=des_decrypt(r['ID']))
        quen.isPublished = True
        quen.publishTime = django.utils.timezone.now()+datetime.timedelta(hours=8)
        quen.save()
    return JsonResponse({'success':True})

def recycle(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = Questionnaire.objects.get(id=des_decrypt(r['ID']))
        quen.isDeleted = True
        quen.save()
    return JsonResponse({'success': True})

def recover(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = Questionnaire.objects.get(id=des_decrypt(r['ID']))
        quen.isDeleted = False
        quen.save()
    return JsonResponse({'success': True})

def suspend(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = Questionnaire.objects.get(id=des_decrypt(r['ID']))
        quen.isPublished = False
        quen.save()
    return JsonResponse({'success': True})

def clear(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = get_questionnaire(des_decrypt(r['qnid']))
        quen_ins = Questionnaire.objects.get(pk=des_decrypt(r['qnid']))
        quen_ins.recoverNum = 0
        quen_ins.save()
        QList = quen['QList']
        for q in QList:
            type = q['type']
            if type in[0,1,3]:
                choi = ChoiceQuestion.objects.get(id=q['qid'])
                CHAnswer.objects.filter(CH=choi).delete()
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
            elif type == 2:
                comp = Complition.objects.get(pk=q['qid'])
                CMPAnswer.objects.filter(CMP=comp).delete()
                comp.participantsNum = 0
                comp.save()
            elif type == 4:
                loc = LocationQuestion.objects.get(pk=q['qid'])
                LOAnswer.objects.filter(LO=loc).delete()
                loc.participantsNum = 0
                loc.save()
        FillRecord.objects.filter(QUEN=quen_ins).delete()
    return JsonResponse({'success': True})


def independent_result(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print(r)
        quen = Questionnaire.objects.get(pk=des_decrypt(r['qnid']))
        ques_ins = get_ques_ins(qnid=quen.pk)
        print(ques_ins)
        records = FillRecord.objects.filter(QUEN=quen)
        users = []
        for record in records:
            users.append(record.USER)
        print(users)
        resultList = []
        for user in users:
            AnswerList = []
            for ques in ques_ins:
                Answer = {}
                if isinstance(ques,ChoiceQuestion):
                    if ques.isMulti == False:
                        Answer['type'] = 0
                        try:
                            chanswer = CHAnswer.objects.get(USER=user,CH=ques)
                            Answer['answer'] = chanswer.content
                        except :
                            Answer['answer'] = None

                    elif ques.isMulti == True:
                        Answer['type'] = 1
                        try:
                            chanswer = CHAnswer.objects.filter(USER=user,CH=ques)
                            answer = []
                            for ans in chanswer:
                                answer.append(ans.content)
                            Answer['answer'] = answer
                        except :
                            Answer['answer'] = None

                    elif ques.isMulti is None:
                        Answer['type'] = 3
                        try:
                            chanswer = CHAnswer.objects.get(USER=user,CH=ques)
                            Answer['answer'] = chanswer.content
                        except :
                            Answer['answer'] = None

                elif isinstance(ques,Complition):
                    Answer['type'] = 2
                    try:
                        companswer = CMPAnswer.objects.get(USER=user, CMP=ques)
                        Answer['answer'] = companswer.content
                    except :
                        Answer['answer'] = None

                elif isinstance(ques,LocationQuestion):
                    Answer['type'] = 4
                    try:
                        locanswer = LOAnswer.objects.get(USER=user,LO=ques)
                        Answer['answer'] = locanswer.content
                    except :
                        Answer['answer'] = None

                AnswerList.append(Answer)
            result = {}
            result['userName'] = user.name
            result['AnswerList'] = AnswerList
            resultList.append(result)

        return JsonResponse({'resultList':resultList})

def score_stat(request):
    r = simplejson.loads(request.body)
    print(r)

    return JsonResponse({'resultList': resultList})
