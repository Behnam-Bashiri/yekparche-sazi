from rest_framework import serializers

from .models import *

class AccountSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class Base_deviceSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Base_device
        fields = '__all__'

class CpuSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'

class PhoneSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'

class TabletSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Tablet
        fields = '__all__'

class LaptopSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'