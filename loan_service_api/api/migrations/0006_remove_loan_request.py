# Generated by Django 4.0.1 on 2022-01-22 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_requestedloan_loanrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='request',
        ),
    ]
