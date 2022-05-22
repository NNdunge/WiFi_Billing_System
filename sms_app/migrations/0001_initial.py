# Generated by Django 4.0.4 on 2022-05-22 13:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sms_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sms_txt', models.CharField(max_length=50)),
                ('sender_number', models.CharField(max_length=50)),
                ('sent_dt', models.DateTimeField(default=datetime.datetime(2022, 5, 22, 16, 38, 22, 828162))),
            ],
        ),
        migrations.CreateModel(
            name='Voucher_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucherType', models.CharField(max_length=50)),
                ('voucherPrice', models.IntegerField()),
                ('validVoucherTime', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('voucherID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('voucherStatus', models.SmallIntegerField(default=0)),
                ('boughtTime', models.DateTimeField()),
                ('generatedTime', models.DateTimeField(default=datetime.datetime(2022, 5, 22, 16, 38, 22, 828162))),
                ('voucherType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_app.voucher_type')),
            ],
        ),
        migrations.CreateModel(
            name='Sms_out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentTime_dt', models.DateTimeField(default=datetime.datetime(2022, 5, 22, 16, 38, 22, 828162))),
                ('corresponding_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_app.sms_in')),
                ('voucherID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_app.voucher')),
            ],
        ),
    ]
