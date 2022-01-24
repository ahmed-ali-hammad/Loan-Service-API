# Loan-Service-API

This is a django API for a digital loan shop that enables the borrowers to submit a loan request with the desired amount and payback date.
The borrowers then gets an offer from one of the lenders(investors) with the interest rate.
If the borrowers accepts the offer, the API will then check if the lender has the available fund to cover the loan plus the service fees. 
After the loan is fully paid off, the loan status is then changed to complete. 

Celery and Celery-beat are used to schedule the loan payments.

Celery is connected to Django using Redis (message broker). 	
