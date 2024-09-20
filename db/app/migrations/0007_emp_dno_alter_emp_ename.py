# Generated by Django 5.1.1 on 2024-09-20 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_dept_emp'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='dno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.dept'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='ename',
            field=models.CharField(max_length=100),
        ),
    ]
