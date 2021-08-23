from django.shortcuts import render
from prototype.models import Questionnaire,Complition,ChoiceQuestion,Option
import re
# Create your views here.


def connect(LQID,ID):
    if re.match(r'CMP',LQID):
        lcomp = Complition.objects.get(CMPID=LQID)
        lcomp.NQID = ID
        lcomp.save()
    else:
        lchoi = ChoiceQuestion.objects.get(CHID=LQID)
        lchoi.NQID = ID
        lchoi.save()

def complition_create(dict):
    comp = Complition(content=dict['title'])
    comp.save()
    comp.CMPID = 'CMP'+str(comp.id)
    if 'limitNum' in dict:
        comp.limitNum = dict['limitNum']
    comp.save()
    return comp

def option_create(dict):
    op = Option(content=dict['content'])
    if 'score' in dict:
        op.score = dict['score']
    op.save()
    return op

def choice_create(dict):
    choi = ChoiceQuestion(content=dict['title'],isMulti=dict['isMulti'])
    choi.save()
    choi.CHID = 'CH'+str(choi.id)
    choi.save()

    if 'limitNum' in dict:
        choi.limitNum = dict['limitNum']
    if 'LQID' in dict:
        connect(dict['LQID'],choi.CHID)

    if 'option' in dict:
        options = dict['option']
        front_op = option_create(options[0])
        front_op.save()
        choi.FOID = front_op.id
        for i in range(1,len(options)):
            back_op = option_create(options[i])
            print(back_op.id)
            front_op.NOID = back_op.id
            front_op.save()
            front_op = back_op
    choi.save()
    return choi


def questionnaire_create(dict):
    #print(dict)
    #print(dict['share'])
    quesn = Questionnaire(title=dict['title'],isPublished=dict['share'])
    quesn.save()
    QList = dict['QList']
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
        else:
            comp = complition_create(q)
            insList.append(comp)
    print(insList)

    for i in range(0,len(insList)-1):
        if isinstance(insList[i+1],ChoiceQuestion):
            insList[i].NQID = insList[i+1].CHID
            if i == 0:
                quesn.FQID = insList[0].CHID
        else:
            insList[i].NQID = insList[i+1].CMPID
            if i == 0:
                quesn.FQID = insList[0].CMPID
        insList[i].save()
        quesn.save()
    return quesn


def get_questionnaire(QnId):
    questionnaire = Questionnaire.objects.get(pk=QnId)
    que_id = questionnaire.FQID
    next_id = None
    que_dict = {}
    que_dict['qnid'] = QnId
    que_dict['title'] = questionnaire.title
    QList = []
    while True:
        quei = {}
        if re.match(r'CMP',que_id):
           print(que_id)
           comp = Complition.objects.get(CMPID=que_id)
           quei['qid'] = int(que_id.lstrip('CMP'))
           quei['type'] = 2
           quei['title'] = comp.content
           next_id = comp.NQID
        elif re.match(r'CH',que_id):

            choi = ChoiceQuestion.objects.get(CHID=que_id)
            quei['qid'] = int(que_id.lstrip('CH'))
            if choi.FOID is None:
                quei['type'] = 3
                quei['title'] = choi.content
            else:
                print('choi')
                if choi.isMulti == False:
                    quei['type'] = 0
                elif choi.isMulti == True:
                    quei['type'] = 1
                quei['title'] = choi.content
                op = Option.objects.get(pk=choi.FOID)
                option = []
                while True:
                    print(option)
                    op_dict = {}
                    op_dict['oid'] = op.pk
                    op_dict['content'] = op.content
                    option.append(op_dict)
                    if op.NOID:
                        op = Option.objects.get(pk=op.NOID)
                    else:
                        break
                quei['option'] = option
            next_id = choi.NQID


        QList.append(quei)
        if not next_id:
            break
        else:
            que_id = next_id
    que_dict['QList'] = QList
    return que_dict

def delete_questionnaire(dict):
    success = True
    try:
        quesn = Questionnaire.objects.get(pk=dict['qnid'])
        qid = quesn.FQID
        while qid:
            if re.match(r'CMP', qid):
                comp = Complition.objects.get(CMPID=qid)
                qid = comp.NQID
                comp.delete()
            else:
                choi = ChoiceQuestion.objects.get(CHID=qid)
                oid = choi.FOID
                while oid:
                    op = Option.objects.get(pk=oid)
                    oid = op.NOID
                    op.delete()
                qid = choi.NQID
                choi.delete()
        quesn.delete()
    except:
        success = False
    return success

def get_options(choi):
    opList = []
    opid = choi.FOID
    while opid:
        op = Option.objects.get(pk=opid)
        opid = op.NOID
        opList.append(op)
    return opList