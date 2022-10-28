# Generated by Django 2.2.16 on 2022-10-28 07:07

import reviews.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[reviews.validators.validate_name], verbose_name='Username'),
        ),
    ]