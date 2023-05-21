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
from django.shortcuts import get_object_or_404


class TemplateViewSet(viewsets.ModelViewSet):
    ordering_fields = '__all_related__'
    queryset = ''
    serializer_class = ''
    

    def list(self, request):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)