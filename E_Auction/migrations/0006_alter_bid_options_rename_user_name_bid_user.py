# Generated by Django 5.0.7 on 2024-09-24 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_Auction', '0005_delete_result'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ['-a_id', '-bid_amt'], 'verbose_name': 'Bid', 'verbose_name_plural': 'Bids'},
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='User_name',
            new_name='user',
        ),
    ]
