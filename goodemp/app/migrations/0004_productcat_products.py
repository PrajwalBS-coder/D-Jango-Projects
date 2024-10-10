# Generated by Django 5.1.2 on 2024-10-10 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_emp_hiredate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCat',
            fields=[
                ('pcid', models.IntegerField(primary_key=True, serialize=False)),
                ('pctype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mdate', models.DateField()),
                ('mplace', models.CharField(max_length=100)),
                ('pcid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productcat')),
            ],
        ),
    ]
