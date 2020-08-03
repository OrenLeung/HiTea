# Generated by Django 3.0.8 on 2020-08-03 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotCheeseFoam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.CharField(choices=[('a', 'Pearl'), ('b', 'Grass Jelly'), ('c', 'Red Beans'), ('d', 'Coconut Jelly'), ('e', 'Pudding'), ('f', 'Agar Ball'), ('h', 'Aloe'), ('i', 'Popping Boba'), ('j', 'Oreo'), ('k', 'Cheese Foam')], max_length=5)),
                ('sugar', models.CharField(choices=[('a', 'No Sugar'), ('b', '30% Sugar'), ('c', '50% Sugar'), ('d', '80% Sugar'), ('e', '100% Sugar')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Product')),
            ],
        ),
        migrations.CreateModel(
            name='HotFreshFruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.CharField(choices=[('a', 'Pearl'), ('b', 'Grass Jelly'), ('c', 'Red Beans'), ('d', 'Coconut Jelly'), ('e', 'Pudding'), ('f', 'Agar Ball'), ('h', 'Aloe'), ('i', 'Popping Boba'), ('j', 'Oreo'), ('k', 'Cheese Foam')], max_length=5)),
                ('sugar', models.CharField(choices=[('a', 'No Sugar'), ('b', '30% Sugar'), ('c', '50% Sugar'), ('d', '80% Sugar'), ('e', '100% Sugar')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Product')),
            ],
        ),
        migrations.CreateModel(
            name='HotLemonTea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.CharField(choices=[('a', 'Pearl'), ('b', 'Grass Jelly'), ('c', 'Red Beans'), ('d', 'Coconut Jelly'), ('e', 'Pudding'), ('f', 'Agar Ball'), ('h', 'Aloe'), ('i', 'Popping Boba'), ('j', 'Oreo'), ('k', 'Cheese Foam')], max_length=5)),
                ('sugar', models.CharField(choices=[('a', 'No Sugar'), ('b', '30% Sugar'), ('c', '50% Sugar'), ('d', '80% Sugar'), ('e', '100% Sugar')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Product')),
            ],
        ),
        migrations.CreateModel(
            name='HotMilkTea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.CharField(choices=[('a', 'Pearl'), ('b', 'Grass Jelly'), ('c', 'Red Beans'), ('d', 'Coconut Jelly'), ('e', 'Pudding'), ('f', 'Agar Ball'), ('h', 'Aloe'), ('i', 'Popping Boba'), ('j', 'Oreo'), ('k', 'Cheese Foam')], max_length=5)),
                ('sugar', models.CharField(choices=[('a', 'No Sugar'), ('b', '30% Sugar'), ('c', '50% Sugar'), ('d', '80% Sugar'), ('e', '100% Sugar')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Product')),
            ],
        ),
        migrations.CreateModel(
            name='IcedCheeseFoam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.CharField(choices=[('a', 'Pearl'), ('b', 'Grass Jelly'), ('c', 'Red Beans'), ('d', 'Coconut Jelly'), ('e', 'Pudding'), ('f', 'Agar Ball'), ('h', 'Aloe'), ('i', 'Popping Boba'), ('j', 'Oreo'), ('k', 'Cheese Foam')], max_length=5)),
                ('sugar', models.CharField(choices=[('a', 'No Sugar'), ('b', '30% Sugar'), ('c', '50% Sugar'), ('d', '80% Sugar'), ('e', '100% Sugar')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Product')),
            ],
        ),
        migrations.CreateModel(
            name='IcedFreshFruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.CharField(choices=[('a', 'Pearl'), ('b', 'Grass Jelly'), ('c', 'Red Beans'), ('d', 'Coconut Jelly'), ('e', 'Pudding'), ('f', 'Agar Ball'), ('h', 'Aloe'), ('i', 'Popping Boba'), ('j', 'Oreo'), ('k', 'Cheese Foam')], max_length=5)),
                ('sugar', models.CharField(choices=[('a', 'No Sugar'), ('b', '30% Sugar'), ('c', '50% Sugar'), ('d', '80% Sugar'), ('e', '100% Sugar')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Product')),
            ],
        ),
        migrations.CreateModel(
            name='IcedLemonTea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.CharField(choices=[('a', 'Pearl'), ('b', 'Grass Jelly'), ('c', 'Red Beans'), ('d', 'Coconut Jelly'), ('e', 'Pudding'), ('f', 'Agar Ball'), ('h', 'Aloe'), ('i', 'Popping Boba'), ('j', 'Oreo'), ('k', 'Cheese Foam')], max_length=5)),
                ('sugar', models.CharField(choices=[('a', 'No Sugar'), ('b', '30% Sugar'), ('c', '50% Sugar'), ('d', '80% Sugar'), ('e', '100% Sugar')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Product')),
            ],
        ),
        migrations.CreateModel(
            name='IcedMilkTea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.CharField(choices=[('a', 'Pearl'), ('b', 'Grass Jelly'), ('c', 'Red Beans'), ('d', 'Coconut Jelly'), ('e', 'Pudding'), ('f', 'Agar Ball'), ('h', 'Aloe'), ('i', 'Popping Boba'), ('j', 'Oreo'), ('k', 'Cheese Foam')], max_length=5)),
                ('sugar', models.CharField(choices=[('a', 'No Sugar'), ('b', '30% Sugar'), ('c', '50% Sugar'), ('d', '80% Sugar'), ('e', '100% Sugar')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
    ]
