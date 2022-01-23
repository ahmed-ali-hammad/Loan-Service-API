from django.db import models
from account.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Account


class LoanRequest(models.Model):
    borrower = models.ForeignKey(Account, on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    loan_period = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Loan Request'
        verbose_name_plural = 'loan Requests'

    def __str__(self):
        return 'Loan Request From ' + self.borrower.first_name + ' ' +  'on ' + str(self.date)


class LoanOffer(models.Model):
    loan_request = models.OneToOneField(LoanRequest, on_delete = models.CASCADE)
    lender = models.ForeignKey(Account, on_delete= models.CASCADE)
    annual_interest_rate = models.FloatField(null = True, blank = True)
    date = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Loan Offer'
        verbose_name_plural = 'loan Offers'

    def __str__(self):
        return ('Loan offer From ' + 
            self.lender.first_name + ' ' + self.lender.last_name + 
            ' to ' + 
            self.loan_request.borrower.first_name + ' ' + self.loan_request.borrower.last_name +
            ' for ' + '$' + str(self.loan_request.loan_amount)
            )
    @property
    def get_monthly_payment(self):
        monthly_interest_rate = self.annual_interest_rate / 12
        return (self.loan_request.loan_amount / self.loan_request.loan_period) * (1 + monthly_interest_rate)
    
#call back function for the signal
def create_loan_offer(instance, sender, *args, **kwargs):
    lender = Account.objects.get(first_name = 'Investor')

    LoanOffer.objects.create(
        loan_request = instance,
        lender = lender,
        annual_interest_rate = 0.15,
    )
	
#sending the signal to create a Loan Offer when the loan Request is valid
post_save.connect(create_loan_offer, sender = LoanRequest)


class Loan(models.Model):
    offer = models.OneToOneField(LoanOffer, on_delete=models.DO_NOTHING)
    lenme_fee = models.FloatField()
    is_funded = models.BooleanField(default = False)
    payment_number = models.IntegerField(default = 0)
    total_number_of_payments = models.IntegerField()
    is_completed = models.BooleanField(default= False)

    @property
    def get_loan_amount_plus_fees(self):
        return self.offer.loan_request.loan_amount + self.lenme_fee

    def check_fund(self):
        if self.offer.lender.available_balance >  self.get_loan_amount_plus_fees:
            self.is_funded = True
        else:
            pass
