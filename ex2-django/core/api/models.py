from django.db import models
from django.utils.translation import gettext_lazy as _
import hashlib
from datetime import datetime, date

# Create your models here.

class UserState(models.TextChoices):
    IN = 'در حال پاسخگویی', _('in')
    END = 'اتمام سوالات', _('end')
    WAIT = 'در انتظار شروع', _('wait')
    DELETE = 'حذف شده', _('delete')

class User(models.Model):
    StuCode = models.CharField(max_length=255,null=True,blank=True,unique=True)
    Token = models.CharField(max_length=255,null=True,blank=True)
    State = models.CharField(
        max_length=100,
        choices=UserState.choices,
        default=UserState.WAIT, blank=True, null=True
    )
    Index = models.IntegerField(null=True,blank=True,default=0)
    FalseCounter = models.IntegerField(null=True,blank=True,default=0)
    TimeStampQuestion = models.IntegerField(null=True,blank=True,default=-1)
    Round = models.IntegerField(null=True,blank=True,default=1)

    def __str__(self) -> str:
        return 'StudentCode : {} - State : {}'.format(self.StuCode,self.State)
    
    def save(self, *args, **kwargs):
        # set the value of the read_only_field using the regular field
        txt = str(self.StuCode) + str(datetime.now())
        result = hashlib.md5(txt.encode())
        if self.Token == None:
            self.Token = result.hexdigest()

        # call the save() method of the parent
        super(User, self).save(*args, **kwargs)

class Question(models.Model):
    Text = models.TextField(default='',null=True,blank=True)
    Code = models.TextField(default='',null=True,blank=True)
    Option1 = models.CharField(max_length=255,null=True,blank=True)
    Option2 = models.CharField(max_length=255,null=True,blank=True)
    Option3 = models.CharField(max_length=255,null=True,blank=True)
    Option4 = models.CharField(max_length=255,null=True,blank=True)
    Answer = models.IntegerField(null=True,blank=True)
    Level = models.IntegerField(null=True,blank=True)
    Time = models.IntegerField(null=True,blank=True,default=0)

    def __str__(self) -> str:
        return 'Text : {} - Level : {}'.format(self.Text,self.Level)