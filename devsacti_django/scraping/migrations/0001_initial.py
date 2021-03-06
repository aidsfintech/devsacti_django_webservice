# Generated by Django 3.2.5 on 2021-07-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Naverstock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N', models.CharField(max_length=100)),
                ('종목명', models.CharField(max_length=100)),
                ('현재가', models.CharField(max_length=100)),
                ('전일비', models.CharField(max_length=100)),
                ('등락률', models.CharField(max_length=100)),
                ('액면가', models.CharField(max_length=100)),
                ('시가총액', models.CharField(max_length=100)),
                ('상장주식수', models.CharField(max_length=100)),
                ('외국인비율', models.CharField(max_length=100)),
                ('거래량', models.CharField(max_length=100)),
                ('PER', models.CharField(max_length=100)),
                ('ROE', models.CharField(max_length=100)),
            ],
        ),
    ]
