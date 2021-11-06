# Generated by Django 3.2.8 on 2021-11-01 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiretuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('tuber_id', models.ImageField(upload_to='')),
                ('tuber_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('user_id', models.ImageField(blank=True, upload_to='')),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
