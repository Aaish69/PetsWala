# Generated by Django 3.2.8 on 2022-03-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_is_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=True),
        ),
    ]
