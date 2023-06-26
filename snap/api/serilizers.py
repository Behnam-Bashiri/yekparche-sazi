import datetime
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *

from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

# CustomUser = get_user_model()


# class CustomUserSerializer(serializers.ModelSerializer):
#     email = serializers.CharField(
#         write_only=True, validators=[validators.UniqueValidator(
#             message='This email already exists',
#             queryset=CustomUser.objects.all()
#         )]
#     )
#     password = serializers.CharField(write_only=True)
#     gender = serializers.CharField(required=False)
#     last_name = serializers.CharField(required=False)
#     first_name = serializers.CharField(required=False)

#     class Meta:
#         model = CustomUser
#         fields = ('first_name', 'last_name', 'email',
#                   'password', 'gender')


# class CustomUserRetrieveSerializer(serializers.ModelSerializer):
#     gender = serializers.CharField(required=False)

#     class Meta:
#         model = CustomUser
#         fields = ('first_name', 'last_name', 'email',
#                      'gender', 'id','last_login')

class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields =  '__all__'



class CustomDriverSerializers(DriverSerializers):
    class Meta:
        model = Driver
        fields =  ('status',)


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class TripSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
