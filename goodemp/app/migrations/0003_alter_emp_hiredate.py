# Generated by Django 5.1.1 on 2024-09-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_emp_hiredate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='hiredate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
