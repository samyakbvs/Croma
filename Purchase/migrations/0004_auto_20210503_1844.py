# Generated by Django 3.0.3 on 2021-05-03 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0003_suppliers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierinvoice',
            name='Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Purchase.Suppliers'),
        ),
    ]
