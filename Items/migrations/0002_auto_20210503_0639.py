# Generated by Django 3.0.3 on 2021-05-03 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
