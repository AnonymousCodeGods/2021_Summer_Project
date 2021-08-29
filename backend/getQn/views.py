from django.shortcuts import render
from django.http import JsonResponse
import simplejson
from prototype.base_option import get_questionnaire,des_decrypt,des_encrypt

def getQn(request):
    if request.method == 'POST':
        r = simplejson.loads(request.body)
        print("******************r********************")
        print(r)
        QnId = des_decrypt(r['QnId'])
        print("******************getQn********************")
        print(QnId)
        que = get_questionnaire(QnId)
        return JsonResponse({'que':que})