# Generated by Django 3.2.11 on 2022-01-23 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220123_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='monthly_payment',
            new_name='payment_number',
        ),
        migrations.RenameField(
            model_name='loan',
            old_name='number_of_payments',
            new_name='total_number_of_payments',
        ),
    ]
