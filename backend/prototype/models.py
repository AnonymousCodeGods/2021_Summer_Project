from django.db import models
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64,unique=True)
    password = models.CharField(max_length=64)
    mail = models.EmailField(null=True)
    phone = models.CharField(max_length=32,null=True)
    isMale = models.BooleanField(null=True,default=True)
    def __str__(self):
        return self.name

class Questionnaire(models.Model):
    type = models.IntegerField(default=0,null=True)

    USER = models.ForeignKey('User',on_delete=models.CASCADE,null=True)

    publishTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)
    createTime = models.DateTimeField(auto_now_add=True)

    isClose = models.BooleanField(default=False,null=True)
    isDeleted = models.BooleanField(default=False,null=True)
    isPublished = models.BooleanField(default=False,null=True)
    showNumbers = models.BooleanField(default=True,null=True)
    hasBranch = models.BooleanField(default=False,null=True)

    recoverNum = models.IntegerField(default=0,null=True)
    limitNum = models.IntegerField(null=True)

    title = models.CharField(max_length=64,null=True)
    FQID = models.CharField(max_length=64,null=True)
    key = models.CharField(max_length=64,default='panzhita')
    code = models.CharField(max_length=64,null=True,default=None)


    def __str__(self):
        return self.title

class BelongTo(models.Model):
    option = models.IntegerField(default=-1,null=True)
    question = models.IntegerField(default=-1,null=True)
    order = models.IntegerField(default=-1,null=True)

    QUEN = models.ForeignKey('Questionnaire',on_delete=models.CASCADE,null=True)

class Question(models.Model):
    content = models.TextField()

    participantsNum = models.IntegerField(default=0)
    hasLimitNum = models.BooleanField(default=False,null=True)
    score = models.IntegerField(null=True,default=0)

    isRequired = models.BooleanField(null=True,default=True)
    class Meta:
        abstract = True

class Complition(Question):
    CMPID = models.CharField(max_length=64,unique=True)
    NQID = models.CharField(max_length=64)
    def __str__(self):
        return self.CMPID

class ChoiceQuestion(Question):
    CHID = models.CharField(max_length=64,unique=True)
    NQID = models.CharField(max_length=64)
    FOID = models.IntegerField(null=True)
    isMulti = models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.CHID

class LocationQuestion(Question):
    LOID = models.CharField(max_length=64,unique=True)
    NQID = models.CharField(max_length=64)
    def __str__(self):
        return self.LOID

class Option(models.Model):
    NOID = models.IntegerField(null=True)

    content = models.TextField()

    selectedNum = models.IntegerField(default=0,null=True)
    score = models.IntegerField(null=True)
    limitNum = models.IntegerField(null=True)

    isCorrect = models.BooleanField(null=True)

    def __str__(self):
        return 'OP'+str(self.id)

class CMPAnswer(models.Model):
    content = models.TextField(null=True)
    CMP = models.ForeignKey('Complition',on_delete=models.CASCADE,null=True)
    USER = models.ForeignKey('User',on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.content

class CHAnswer(models.Model):
    content = models.IntegerField(null=True)
    CH = models.ForeignKey('ChoiceQuestion',on_delete=models.CASCADE,null=True)
    USER = models.ForeignKey('User',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.content

class LOAnswer(models.Model):
    content = models.TextField(null=True)
    LO = models.ForeignKey('LocationQuestion',on_delete=models.CASCADE,null=True)
    USER = models.ForeignKey('User',on_delete=models.CASCADE,null=True)

class StarNum(models.Model):
    CH = models.ForeignKey('ChoiceQuestion',on_delete=models.CASCADE,null=True)

    zero_star = models.IntegerField(null=True,default=0)
    one_star = models.IntegerField(null=True,default=0)
    two_star = models.IntegerField(null=True,default=0)
    three_star = models.IntegerField(null=True,default=0)
    four_star = models.IntegerField(null=True,default=0)
    five_star = models.IntegerField(null=True,default=0)

class FillRecord(models.Model):
    USER = models.ForeignKey('User',on_delete=models.CASCADE)
    QUEN = models.ForeignKey('Questionnaire',on_delete=models.CASCADE)

    fillTime = models.DateTimeField()

