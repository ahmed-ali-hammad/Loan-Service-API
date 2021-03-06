# Generated by Django 4.0.1 on 2022-01-22 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_loanoffer_annual_interest_rate_loanoffer_loan_amount_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loanoffer',
            options={'verbose_name': 'Loan Offer', 'verbose_name_plural': 'loan Offers'},
        ),
        migrations.AlterModelOptions(
            name='requestedloan',
            options={'verbose_name': 'Loan Request', 'verbose_name_plural': 'loan Requests'},
        ),
        migrations.RenameField(
            model_name='loanoffer',
            old_name='initiation_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='loanoffer',
            name='is_accepted',
        ),
        migrations.RemoveField(
            model_name='loanoffer',
            name='loan_amount',
        ),
    ]
