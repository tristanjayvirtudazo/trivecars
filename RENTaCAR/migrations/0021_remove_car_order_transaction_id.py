# Generated by Django 3.1.7 on 2021-05-05 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RENTaCAR', '0020_auto_20210504_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_order',
            name='transaction_id',
        ),
    ]
