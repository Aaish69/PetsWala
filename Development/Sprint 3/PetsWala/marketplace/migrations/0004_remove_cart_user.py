# Generated by Django 3.2.9 on 2022-03-31 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_auto_20220331_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
