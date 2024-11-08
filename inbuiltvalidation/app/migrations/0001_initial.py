# Generated by Django 5.1.2 on 2024-11-08 08:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllinOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator('Invalid Email')])),
                ('url', models.URLField(validators=[django.core.validators.URLValidator])),
            ],
        ),
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sid', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
