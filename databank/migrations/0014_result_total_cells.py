# Generated by Django 2.1 on 2018-09-10 09:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databank', '0013_auto_20180910_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='total_cells',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(400)]),
        ),
    ]
