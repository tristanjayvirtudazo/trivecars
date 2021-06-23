# Generated by Django 3.1.7 on 2021-04-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=50)),
                ('birthd_ate', models.DateField()),
                ('gender_male', models.BooleanField()),
                ('gender_female', models.BooleanField()),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('barangay', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('contact_num', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('password_confirm', models.CharField(max_length=100)),
            ],
        ),
    ]
