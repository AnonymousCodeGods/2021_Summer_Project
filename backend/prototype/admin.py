from django.contrib import admin
from .models import Questionnaire,ChoiceQuestion,Complition,User,Option,StarNum,CMPAnswer
# Register your models here.
admin.site.register(Questionnaire)
admin.site.register(ChoiceQuestion)
admin.site.register(Complition)
admin.site.register(User)
admin.site.register(Option)
admin.site.register(StarNum)
admin.site.register(CMPAnswer)