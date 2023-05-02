from dataclasses import fields
import datetime
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *
from django.apps import apps


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('StuCode','State','Index','FalseCounter','TimeStampQuestion')

class CretaeUserCustom(UserSerializers):
    class Meta:
        model = User
        fields = ('id','StuCode','Token')

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class GetQuestionCustom(QuestionSerializers):
    class Meta:
        model = Question
        fields = ('id','Text','Code','Option1','Option2','Option3','Option4','Time')

        