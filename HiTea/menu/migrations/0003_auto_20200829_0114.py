# Generated by Django 3.1 on 2020-08-29 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200829_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=32),
        ),
    ]