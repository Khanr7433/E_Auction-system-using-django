# Generated by Django 5.0.7 on 2024-09-24 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_Auction', '0009_result_end_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='end_time',
            new_name='end_datetime',
        ),
    ]
