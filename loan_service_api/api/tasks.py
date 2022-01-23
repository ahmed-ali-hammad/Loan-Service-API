from time import perf_counter_ns
from celery import shared_task
from .models import *
from django_celery_beat.models import PeriodicTask


@shared_task(bind=True)
def pay_loan(self):
    loan = Loan.objects.all().last()
    loan.payment_number += 1
    loan.save()
    if loan.payment_number == loan.total_number_of_payments:
        periodic_task = PeriodicTask.objects.all().last()
        periodic_task.enabled = False
        loan.is_completed = True
        periodic_task.save()
        loan.save()
    return "Done"