from rest_framework import serializers
from .models import AccountModels

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModels
        fields = '__all__'