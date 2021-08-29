from prototype.base_option import get_ques_ins,get_op_ins,des_decrypt,des_encrypt
from prototype.models import *
import django.utils.timezone
import datetime

def now_time():
    return django.utils.timezone.now()+datetime.timedelta(hours=8)

def fill_single(choi,answer,user):
    options = get_op_ins(choi)
    if answer is None:
        ans_ins = CHAnswer(content=answer, USER=user, CH=choi)
        ans_ins.save()
        return
    opi = options[answer]
    sNum = opi.selectedNum
    opi.selectedNum = sNum + 1
    opi.save()
    ans_ins = CHAnswer(content=answer, USER=user, CH=choi)
    ans_ins.save()
    return

def fill_multi(choi,answer,user):
    options = get_op_ins(choi)
    if answer is None:
        ans_ins = CHAnswer(content=answer, USER=user, CH=choi)
        ans_ins.save()
        return
    for a in answer:
        opi = options[a]
        sNum = opi.selectedNum
        opi.selectedNum = sNum + 1
        opi.save()
        ans_ins = CHAnswer(content=a, USER=user, CH=choi)
        ans_ins.save()
    return

def fill_comp(comp,answer,user):
    p = comp.participantsNum
    comp.participantsNum = p + 1
    comp.save()
    ans_ins = CMPAnswer(content=answer, USER=user, CMP=comp)
    ans_ins.save()
    return

def fill_star(choi,answer,user):
    try:
        starNum = StarNum.objects.get(CH=choi)
    except:
        starNum = StarNum(CH=choi)
        starNum.save()

    ans_ins = CHAnswer(content=answer, USER=user, CH=choi)
    ans_ins.save()

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
    return

def fill_loc(loc,answer,user):
    p = loc.participantsNum
    loc.participantsNum = p + 1
    loc.save()
    ans_ins = LOAnswer(content=answer, LO=loc, USER=user)
    ans_ins.save()
    return



def ordi_submit(r):
    qnid = des_decrypt(r['qnId'])
    quesn_ins = Questionnaire.objects.get(pk=qnid)
    if quesn_ins.endTime is not None and now_time() > quesn_ins.endTime:
        return False
    ques_ins = get_ques_ins(qnid)
    AnswerList = r['AnswerList']
    user = None
    try:
        user = User.objects.get(name=r['userName'])
        f_record = FillRecord.objects.filter(QUEN=quesn_ins,USER=user)
        if len(f_record) == 1 and ques_ins.type != 0:
            return False
    except:
        now = now_time()
        key = str(now)+str(qnid)
        user = User(name=key,password=key)
        user.save()
    print(user)
    for ques,Answer in zip(ques_ins,AnswerList):
        type = Answer['type']
        answer = Answer['answer']
        if type == 0:
            fill_single(ques,answer,user)
        elif type == 1:
            fill_multi(ques,answer,user)
        elif type == 2:
            fill_comp(ques,answer,user)
        elif type == 3:
            fill_star(ques,answer,user)
        elif type == 4:
            fill_loc(ques,answer,user)
    record = FillRecord(USER=user,fillTime=now_time(),QUEN=quesn_ins)
    record.save()
    rnum = quesn_ins.recoverNum
    quesn_ins.recoverNum = rnum + 1
    quesn_ins.save()
    return True

def sign_submit(r):
    condition = {}
    qnid = des_decrypt(r['qnId'])
    quesn_ins = Questionnaire.objects.get(pk=qnid)
    if quesn_ins.endTime is not None and now_time() > quesn_ins.endTime:
        condition['timeOut'] = True
        return condition
    user = User.objects.get(name=r['userName'])

    user = User.objects.get(name=r['userName'])
    f_record = FillRecord.objects.filter(QUEN=quesn_ins, USER=user)
    if len(f_record) == 1:
        condition['success'] = False
        condition['msg'] = 0
        condition['type'] = 5
        return condition

    if quesn_ins.limitNum is not None:
        if quesn_ins.limitNum == quesn_ins.recoverNum:
            condition['success'] = False
            condition['msg'] = 0
            condition['type'] = 1
            return condition
    ques_ins = get_ques_ins(qnid)
    AnswerList = r['AnswerList']
    for ques, Answer in zip(ques_ins, AnswerList):
        if Answer['type'] in [0,1]:
            if ques.hasLimitNum == True and ques.isRequired == True:
                options = get_op_ins(ques)
                flag = True
                for option in options:
                    if  option.limitNum is not None and option.selectedNum == option.limitNum:
                        flag = False
                if flag == False:
                    condition['success'] = False
                    condition['msg'] = 0
                    condition['type'] = 2
                    return condition

    for ques, Answer in zip(ques_ins, AnswerList):
        if Answer['type'] in [0,1]:
            options = get_op_ins(ques)
            answer = Answer['answer']

            if Answer['type'] == 0:
                if answer is not None and options[answer].limitNum is not None and options[answer].limitNum == options[answer].selectedNum:
                    condition['success'] = False
                    condition['msg'] = 1
                    condition['type'] = 3
                    return condition
            elif Answer['type'] == 1:
                for a in answer:
                    if answer is not None and options[a].limitNum is not None and options[a].limitNum == options[a].selectedNum:
                        condition['success'] = False
                        condition['msg'] = 1
                        condition['type'] = 4
                        return condition
    ordi_submit(r)
    condition['success'] = True
    condition['msg'] = -1
    return condition
