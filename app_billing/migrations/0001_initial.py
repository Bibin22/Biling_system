# Generated by Django 3.1.7 on 2021-03-11 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_qty', models.IntegerField(default=0)),
                ('purchase_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_billing.items')),
            ],
        ),
    ]
