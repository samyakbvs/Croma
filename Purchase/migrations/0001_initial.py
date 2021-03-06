# Generated by Django 3.0.3 on 2021-05-02 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=264)),
                ('Inv_num', models.BigIntegerField(unique=True)),
                ('Date', models.DateField()),
                ('Doc_num', models.BigIntegerField()),
                ('Doc_date', models.DateField()),
                ('Mode', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='ItemsPurchased',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='0', max_length=264)),
                ('quantity', models.BigIntegerField()),
                ('quantity_free', models.BigIntegerField()),
                ('price', models.BigIntegerField()),
                ('sgst', models.BigIntegerField()),
                ('cgst', models.BigIntegerField()),
                ('discount', models.BigIntegerField()),
                ('amount', models.BigIntegerField(default=0)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Purchase.SupplierInvoice')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Items.Item')),
            ],
        ),
    ]
