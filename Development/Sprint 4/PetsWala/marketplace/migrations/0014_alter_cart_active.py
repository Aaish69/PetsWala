# Generated by Django 3.2.9 on 2022-04-22 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0013_order_placed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]