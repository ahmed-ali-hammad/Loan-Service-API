from django.contrib import admin
from .models import *


admin.site.register(LoanRequest)
admin.site.register(LoanOffer)
admin.site.register(Loan)