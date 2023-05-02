from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import status
from rest_framework.serializers import Serializer
from .serilizers import *
from rest_framework import filters
from .models import *
from .serilizers import *
from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissions
from datetime import datetime, date
# from base_models.models.Base
import json
import pytz
from django.shortcuts import get_object_or_404


# Create your views here.


class TemplateViewSet(viewsets.ModelViewSet):
    search_fields = []
    ordering_fields = '__all_related__'
    user_profile_model = None

    def list(self, request):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class UserList(TemplateViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    # permission_classes = [DjangoModelPermissions]

    def list(self, request):
        query = User.objects.all().order_by('-TimeStampQuestion')
        serializer = UserListSerializers(query, many=True)
        return JsonResponse({'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request):
        StudentCode = request.data.get('StuCode')
        try:
            objStudent = User.objects.get(StuCode=StudentCode)
            return JsonResponse({'message': 'نام کاربری از قبل وجود دارد'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except User.DoesNotExist:
            print("this : {}".format(StudentCode))
            objStudent = User.objects.create(StuCode=StudentCode)
            objStudent.save()
            serializer = CretaeUserCustom(objStudent)
            return JsonResponse({'message':'کاربر ایجاد شد','data': serializer.data}, status=status.HTTP_200_OK)
    
    def destroy(self, request): 
        StudentCode = request.data.get('StuCode')
        UserToken = request.data.get('Token')
        try:
            objStudent = User.objects.get(StuCode=StudentCode)
            if objStudent.Token == UserToken:
                objStudent.State = UserState.DELETE
                objStudent.save()
                return JsonResponse({'message':'کاربر حذف شد'}, status=status.HTTP_423_LOCKED)
            else:
                return JsonResponse({'message': 'توکن شما منضقی شده است'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return JsonResponse({'message': 'نام کاربری وجود ندارد'}, status=status.HTTP_406_NOT_ACCEPTABLE)

class QuestionList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    # permission_classes = [DjangoModelPermissions]

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        page_result = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page_result, many=True)
        return JsonResponse({'count': count, 'data': serializer.data}, status=status.HTTP_200_OK)
    
    @action(methods=['post'],detail=False)
    def GetQuestions(self,request):
        UserToken = request.data.get('Token')
        StuCode = request.data.get('StuCode')
        QuestionLevel = request.data.get('Level')

        user = User.objects.get(StuCode=StuCode)
        if user.Token == UserToken:
            user.State = UserState.IN
            user.save()
            if user.Round == QuestionLevel:
                questions = Question.objects.filter(Level=QuestionLevel)
                serializer = GetQuestionCustom(questions, many=True)
                return JsonResponse({'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'message': 'شما مجوز ورود به این مرحله را ندارید'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse({'message': 'توکن شما منضقی شده است'}, status=status.HTTP_401_UNAUTHORIZED)
        
    @action(methods=['post'],detail=False)
    def Answerd(self,request):
        UserToken = request.data.get('Token')
        StuCode = request.data.get('StuCode')
        QuestionID = request.data.get('QuestionID')
        Answer = request.data.get('Answer') #True 1 , False 0
        TimeStamp = request.data.get('TimeStamp')

        user = User.objects.get(StuCode=StuCode)
        if user.Token == UserToken:
            try:
                question_selector = Question.objects.get(id=QuestionID)
                CA = question_selector.Answer
                if CA == int(Answer):
                    user.Index += 1
                    if TimeStamp != -1:
                        user.TimeStampQuestion = TimeStamp
                        user.save()
                    user.save()
                else:
                    user.Index += 1
                    user.FalseCounter += 1
                    if TimeStamp != -1:
                        user.TimeStampQuestion = TimeStamp
                        user.save()
                    user.save()
                    user = User.objects.get(StuCode=StuCode)
                    if user.FalseCounter >= 3:
                        user.State = UserState.DELETE
                        user.save()
                        return JsonResponse({'message':'کاربر حذف شد'}, status=status.HTTP_423_LOCKED)
                return JsonResponse({'message':'پاسخ ثبت شد'}, status=status.HTTP_200_OK)
            except Question.DoesNotExist:
                return JsonResponse({'message': 'سوال یافت نشد'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse({'message': 'توکن شما منضقی شده است'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['post'],detail=False)
    def End(self,request):
        UserToken = request.data.get('Token')
        StuCode = request.data.get('StuCode')

        user = User.objects.get(StuCode=StuCode)
        if user.Token == UserToken:
            user.State = UserState.END
            if user.Round == 1:
                user.Round = 2
            else :
                user.Round = 3
            user.save()
            return JsonResponse({'message':'شما با موفقیت این مرحله را پشت سر گذاشته اید'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'توکن شما منضقی شده است'}, status=status.HTTP_401_UNAUTHORIZED)
