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
    
class AccountList(TemplateViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerlizer
    # permission_classes = [DjangoModelPermissions]


class Base_deviceList(TemplateViewSet):
    queryset = Base_device.objects.all()
    serializer_class = Base_deviceSerlizer
    # permission_classes = [DjangoModelPermissions]

class LaptopList(TemplateViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerlizer
    # permission_classes = [DjangoModelPermissions]

class TabletList(TemplateViewSet):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerlizer
    # permission_classes = [DjangoModelPermissions]

class PhoneList(TemplateViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerlizer
    # permission_classes = [DjangoModelPermissions]

class CpuList(TemplateViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerlizer
    # permission_classes = [DjangoModelPermissions]