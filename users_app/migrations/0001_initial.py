# Generated by Django 4.0.4 on 2022-05-22 13:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('location', models.TextField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 22, 13, 38, 22, 830123, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 5, 22, 13, 38, 22, 830123, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='VoucherRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('voucherType', models.CharField(choices=[('pawa20', 'pawa20'), ('pawa50', 'pawa50'), ('pawa100', 'pawa100'), ('wazito200', 'wazito200'), ('boss500', 'boss500'), ('GOAT1000', 'GOAT1000')], max_length=20)),
                ('voucherPrice', models.IntegerField()),
                ('device', models.TextField(choices=[('Laptop', 'Laptop'), ('Mobile Phone', 'Mobile Phone')])),
            ],
        ),
    ]
