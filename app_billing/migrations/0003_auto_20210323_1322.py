# Generated by Django 3.1.7 on 2021-03-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_billing', '0002_auto_20210312_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billnumber',
            field=models.CharField(max_length=12),
        ),
    ]
