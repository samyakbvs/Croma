# Generated by Django 3.0.3 on 2021-05-03 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0003_auto_20210503_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyerinvoice',
            old_name='Final_Amount',
            new_name='Final_amount',
        ),
    ]
