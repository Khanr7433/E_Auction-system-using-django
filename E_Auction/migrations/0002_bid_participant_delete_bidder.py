# Generated by Django 5.0.7 on 2024-09-16 16:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Auction', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Bidder id')),
                ('bid_amt', models.IntegerField(verbose_name='Bid Amount')),
                ('bid_time', models.DateTimeField(auto_now_add=True, verbose_name='Bid Time')),
                ('User_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Bidder Name')),
                ('a_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Auction.auction', verbose_name='Auction id')),
            ],
            options={
                'verbose_name': 'Bid',
                'verbose_name_plural': 'Bids',
                'db_table': 'bids',
                'ordering': ['-a_id', '-bid_amt', '-bid_time'],
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Participant Id')),
                ('User_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Bidder Name')),
                ('a_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Auction.auction', verbose_name='Auction id')),
            ],
            options={
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Partcipants',
                'db_table': 'participant',
                'ordering': ['-p_id'],
            },
        ),
        migrations.DeleteModel(
            name='Bidder',
        ),
    ]
