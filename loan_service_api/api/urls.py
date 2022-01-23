from django.urls import path
from .views import *

urlpatterns = [
    path('loan-request/', loan_request.as_view(), name = "loan_request"),
    path('loan-initiate/<amount>/', loan_initiate , name = "loan_initiate"),
]
