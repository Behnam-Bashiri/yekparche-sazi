import datetime
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *


class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


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
