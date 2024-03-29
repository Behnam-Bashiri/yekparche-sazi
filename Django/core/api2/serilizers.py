from rest_framework import serializers

from .models import *

class AccountSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class CustomAccountSerlizer(AccountSerlizer):
    class Meta:
        model = Account
        fields = ('Name','Phone')

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

    def to_representation(self,instance):
        response =super().to_representation(instance)
        # response['Cpu'] = CpuSerlizer(instance.cpu).data['core']
        # response['WT'] = 'yekparchesazi'
        return response
    