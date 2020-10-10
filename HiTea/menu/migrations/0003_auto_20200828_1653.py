# Generated by Django 3.1 on 2020-08-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200828_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='freshfruit',
            name='isHot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='freshfruit',
            name='toppings',
            field=models.ManyToManyField(null=True, to='menu.Topping'),
        ),
        migrations.AlterField(
            model_name='cheesefoam',
            name='toppings',
            field=models.ManyToManyField(null=True, to='menu.Topping'),
        ),
        migrations.AlterField(
            model_name='lemontea',
            name='toppings',
            field=models.ManyToManyField(null=True, to='menu.Topping'),
        ),
        migrations.AlterField(
            model_name='milktea',
            name='toppings',
            field=models.ManyToManyField(null=True, to='menu.Topping'),
        ),
    ]