from django.shortcuts import render
from prototype.models import *
import re

# Create your views here.
import django.utils.timezone
import datetime

import binascii
from pyDes import des, CBC, PAD_PKCS5

secret_key = 'panzhita'

def des_encrypt(qnid):
    quen = Questionnaire.objects.get(pk=qnid)
    iv = quen.key
    s = str(qnid).rjust(8,'0')
    k = des(quen.key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    encoded = binascii.b2a_hex(en).decode()
    quen.code = encoded
    quen.save()
    return encoded


def des_decrypt(s):
    quen = Questionnaire.objects.get(code=s)
    return quen.pk



def des_encrypt_demo(qnid):
    iv = secret_key
    s = str(qnid).rjust(8,'0')
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en).decode()


def connect(LQID,ID):
    if re.match(r'CMP',LQID):
        lcomp = Complition.objects.get(CMPID=LQID)
        lcomp.NQID = ID
        lcomp.save()
    elif re.match(r'CMP',LQID):
        lchoi = ChoiceQuestion.objects.get(CHID=LQID)
        lchoi.NQID = ID
        lchoi.save()
    elif re.match(r'LO',LQID):
        lloc = LocationQuestion.objects.get(CHID=LQID)
        lloc.NQID = ID
        lloc.save()

def complition_create(dict):
    comp = Complition(content=dict['title'])
    if 'necessary' in dict:
        comp.isRequired = dict['necessary']
    comp.save()
    comp.CMPID = 'CMP'+str(comp.id)
    if 'limitNum' in dict:
        comp.limitNum = dict['limitNum']
    comp.save()
    return comp

def lock_create(dict):
    loc = LocationQuestion(content=dict['title'])
    if 'necessary' in dict:
        loc.isRequired = dict['necessary']
    loc.save()
    loc.LOID = 'LO'+str(loc.id)
    if 'limitNum' in dict:
        loc.limitNum = dict['limitNum']
    loc.save()
    return loc


def option_create(dict):
    op = Option(content=dict['content'])
    if 'score' in dict:
        op.score = dict['score']
    op.save()
    return op

def choice_create(dict):
    choi = ChoiceQuestion(content=dict['title'],isMulti=dict['isMulti'])
    if 'necessary' in dict:
        choi.isRequired = dict['necessary']
    
    choi.save()
    choi.CHID = 'CH'+str(choi.id)
    choi.save()
    limit_flag = False
    if 'limitNum' in dict:
        choi.limitNum = dict['limitNum']
    if 'LQID' in dict:
        connect(dict['LQID'],choi.CHID)
    if 'isSumLimit' in dict and dict['isSumLimit'] == True:
        choi.hasLimitNum = True
        limit_flag = True
        choi.save()
    
    
    if 'option' in dict:
        op_ins = []
        options = dict['option']
        front_op = option_create(options[0])
        if limit_flag:
            front_op.limitNum = options[0]['limit']
        front_op.save()
        op_ins.append(front_op)
        choi.FOID = front_op.id
        for i in range(1,len(options)):
            back_op = option_create(options[i])
            front_op.NOID = back_op.id
            if limit_flag:
                back_op.limitNum = options[i]['limit']
                back_op.save()
            op_ins.append(back_op)
            front_op.save()
            front_op = back_op
    
    choi.save()
    if 'hasAnswer' in dict and dict['hasAnswer'] == True:
        if dict['type'] == 0:
            op = op_ins[dict['Answer']]
            op.isCorrect = True
            op.save()
        elif dict['type'] == 1:
            for a in dict['Answer']:
                op = op_ins[a]
                op.isCorrect = True
                op.save()
                pass
        pass
    if choi.isMulti is None:
        star = StarNum(CH=choi)
        star.save()
    return choi

def questionnaire_create(dict):
    quesn = Questionnaire(title=dict['title'],USER=dict['user'],type=dict['qnType'],showNumbers=dict['showNumbers'])
    quesn.save()
    quesn.code = des_encrypt_demo(quesn.pk)
    quesn.save()
    if 'isSumLimit' in dict:
        if dict['isSumLimit'] == True:
            quesn.limitNum = dict['limit']
            quesn.save()
            pass
    quesn.publishTime = "2000-01-01T12:00:00.000Z"
    quesn.save()
    QList = dict['QList']
    if len(QList) == 0:
        return quesn
    insList = []
    for q in  QList:
        if q['type'] in [0,1,3]:
            type = q['type']
            isMulti = None
            if type == 0:
                isMulti = False
            elif type == 1:
                isMulti = True
            q['isMulti'] = isMulti
            choi = choice_create(q)
            insList.append(choi)
        elif q['type'] == 2:
            comp = complition_create(q)
            insList.append(comp)
        elif q['type'] == 4:
            loc = lock_create(q)
            insList.append(loc)

    if isinstance(insList[0], ChoiceQuestion):
        quesn.FQID = insList[0].CHID
    elif isinstance(insList[0], Complition):
        quesn.FQID = insList[0].CMPID
    elif isinstance(insList[0], LocationQuestion):
        quesn.FQID = insList[0].LOID

    for i in range(0,len(insList)-1):
        if isinstance(insList[i+1],ChoiceQuestion):
            insList[i].NQID = insList[i+1].CHID

        elif isinstance(insList[i+1],Complition):
            insList[i].NQID = insList[i+1].CMPID

        elif isinstance(insList[i+1],LocationQuestion):
            insList[i].NQID = insList[i+1].LOID

        insList[i].save()
    quesn.save()

    if 'hasBranch' in dict and dict['hasBranch'] == True:
        quesn.hasBranch = True
        quesn.save()
        i = 0
        for Ques in QList:
            if 'belongTo' in Ques:
                relation = Ques['belongTo']
                qid = relation['qid']
                option_id = relation['option']
                if qid != -1:
                    b = BelongTo(question=qid,option=option_id,QUEN=quesn,order=i)
                    b.save()
            i = i + 1
    return quesn


def get_questionnaire(QnId):
    questionnaire = Questionnaire.objects.get(pk=QnId)
    now_time = django.utils.timezone.now()+datetime.timedelta(hours=8)
    if questionnaire.endTime is not None and now_time > questionnaire.endTime:
        questionnaire.isPublished = False
        questionnaire.save()
        pass
    que_id = questionnaire.FQID
    t = questionnaire.createTime+datetime.timedelta(hours=8)
    next_id = None
    que_dict = {}
    que_dict['qnid'] = des_encrypt(QnId)
    que_dict['title'] = questionnaire.title
    que_dict['state'] = questionnaire.isPublished
    que_dict['pubTime'] = questionnaire.publishTime
    que_dict['endTime'] = questionnaire.endTime
    que_dict['qnType'] = questionnaire.type
    que_dict['showNumbers'] = questionnaire.showNumbers
    if questionnaire.type == 3 and questionnaire.endTime is not None:
        now_time = django.utils.timezone.now()+datetime.timedelta(hours=8)
        que_dict['remainTime'] =  int((questionnaire.endTime - now_time).total_seconds())
        pass
    if questionnaire.limitNum:
        que_dict['isSumLimit'] = True
    else:
        que_dict['isSumLimit'] = False
    que_dict['limit'] = questionnaire.recoverNum


    QList = []
    if que_id:
        while True:
            quei = {}
            quei['total'] = 0
            if re.match(r'CMP',que_id):
               comp = Complition.objects.get(CMPID=que_id)
               quei['qid'] = int(que_id.lstrip('CMP'))
               quei['type'] = 2
               quei['title'] = comp.content
               quei['necessary'] = comp.isRequired
               next_id = comp.NQID
            elif re.match(r'CH',que_id):
                choi = ChoiceQuestion.objects.get(CHID=que_id)
                quei['qid'] = int(que_id.lstrip('CH'))
                quei['necessary'] = choi.isRequired
                if choi.hasLimitNum == True:
                    quei['isSumLimit'] = True
                else:
                    quei['isSumLimit'] = False
                if choi.FOID is None:
                    quei['type'] = 3
                    quei['title'] = choi.content
                else:
                    if choi.isMulti == False:
                        quei['type'] = 0
                    elif choi.isMulti == True:
                        quei['type'] = 1
                    quei['title'] = choi.content
                    op = Option.objects.get(pk=choi.FOID)
                    option = []
                    while True:
                        op_dict = {}
                        op_dict['oid'] = op.pk
                        op_dict['content'] = op.content
                        op_dict['count'] = 0
                        op_dict['percentage'] = 0
                        if op.limitNum is not None:
                            op_dict['limit'] = op.limitNum-op.selectedNum
                        else:
                            op_dict['limit'] = op.limitNum
                        option.append(op_dict)
                        if op.NOID:
                            op = Option.objects.get(pk=op.NOID)
                        else:
                            break
                    quei['option'] = option
                next_id = choi.NQID

            elif re.match(r'LO', que_id):
                loc = LocationQuestion.objects.get(LOID=que_id)
                quei['qid'] = int(que_id.lstrip('LO'))
                quei['type'] = 4
                quei['title'] = loc.content
                quei['necessary'] = loc.isRequired
                next_id = loc.NQID

            QList.append(quei)
            if not next_id:
                break
            else:
                que_id = next_id


    for Ql in QList:
        belongTo = {}
        belongTo['qid'] = -1
        belongTo['option'] = -1
        Ql['belongTo'] = belongTo


    if questionnaire.hasBranch == True:
        belongs = BelongTo.objects.filter(QUEN=questionnaire)
        for belong in belongs:
            i = belong.order
            belongTo = {}
            belongTo['qid'] = belong.question
            belongTo['option'] = belong.option
            QList[i]['belongTo'] = belongTo

    que_dict['QList'] = QList
    return que_dict

def delete_questionnaire(dict):
    success = True
    try:
        print(dict)
        quesn = Questionnaire.objects.get(pk=dict['qnid'])
        ques_ins = get_ques_ins(dict['qnid'])
        for ques in ques_ins:
            if isinstance(ques, ChoiceQuestion):
                if ques.isMulti is None:
                    starNum = StarNum.objects.get(CH=ques)
                    starNum.delete()
                else:
                    op_ins = get_options(ques)
                    for op in op_ins:
                        op.delete()
            elif isinstance(ques, Complition):
                CMPAnswer.objects.filter(CMP=ques).delete()

            elif isinstance(ques, LocationQuestion):
                LOAnswer.objects.filter(LO=ques).delete()

            ques.delete()
    except:
        success = False
    print(quesn)
    quesn.delete()
    return success

def get_options(choi):
    opList = []
    opid = choi.FOID
    while opid:
        op = Option.objects.get(pk=opid)
        opid = op.NOID
        opList.append(op)
    return opList

def get_ques_ins(qnid):
    ques_ins = []
    quen = Questionnaire.objects.get(pk=qnid)
    qid = quen.FQID
    while qid:
        if re.match(r'CMP', qid):
            ques = Complition.objects.get(CMPID=qid)
        elif re.match(r'CH', qid):
            ques = ChoiceQuestion.objects.get(CHID=qid)
        elif re.match(r'LO', qid):
            ques = LocationQuestion.objects.get(LOID=qid)
        qid = ques.NQID
        ques_ins.append(ques)
    return ques_ins

def get_op_ins(choi):
    op_ins = []
    oid = choi.FOID
    while oid:
        op = Option.objects.get(pk=oid)
        oid = op.NOID
        op_ins.append(op)
    return op_ins