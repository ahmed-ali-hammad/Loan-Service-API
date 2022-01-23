from dataclasses import field
from rest_framework import serializers
from account.models import *
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'full_name']

class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = '__all__'


class LoanOfferSerializer(serializers.ModelSerializer):
    loan_request = LoanRequestSerializer()
    lender = AccountSerializer()
    class Meta:
        model = LoanOffer
        fields = '__all__'