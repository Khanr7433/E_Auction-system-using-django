# Generated by Django 5.0.7 on 2024-09-24 11:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Auction', '0008_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]