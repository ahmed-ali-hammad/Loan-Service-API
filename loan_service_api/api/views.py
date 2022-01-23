from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from  .serializers import *
from django.urls import reverse
from django.http import JsonResponse
from .tasks import *
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from random import randint

class loan_request(APIView):

    serializer_class = LoanRequestSerializer

    def post(self, request):
        serializer = LoanRequestSerializer (data = request.data)
        if serializer.is_valid():
            serializer.save()
            loan_offer = LoanOffer.objects.filter(loan_request__borrower = serializer.validated_data['borrower']).last()
    
            return Response ({'Message':'Here is your loan offer information', 
                'Offer':{
                    'Lender':loan_offer.lender.full_name,
                    'Amount':loan_offer.loan_request.loan_amount,
                    'Annul Interest rate':str(loan_offer.annual_interest_rate * 100) + '%' ,
                    'Monthly Payment': str(loan_offer.get_monthly_payment) + '$',
                    'Payment Plan':str(loan_offer.loan_request.loan_period) + ' months'
                        }, 
                'If you would like to proceed with this offer, please visit the following link': 
                request.build_absolute_uri(reverse('loan_initiate', args=(loan_offer.loan_request.loan_amount,)))
            }, status = status.HTTP_200_OK )
            
        return Response (serializer.data, status = status.HTTP_400_BAD_REQUEST )
        
def loan_initiate(request, amount):
    loan_offer = LoanOffer.objects.all().last()
    loan = Loan.objects.create(
                offer = loan_offer,
                lenme_fee = 4,
                total_number_of_payments = loan_offer.loan_request.loan_period
            )

    loan.check_fund()
    loan.save()

    if loan.is_funded:
        # Payment Scheduale
        value = randint(0, 1000000000)
        schedule, created = CrontabSchedule.objects.get_or_create(day_of_month='1')
        task = PeriodicTask.objects.create(crontab = schedule, name = f'Collect_loan_payment_{value}', task = 'api.tasks.pay_loan',)
    return JsonResponse({'Message': f'your loan for ${amount} has been initiated'})
