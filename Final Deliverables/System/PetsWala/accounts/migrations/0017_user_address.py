# Generated by Django 3.2.9 on 2022-04-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20220409_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='ABC', max_length=100),
        ),
    ]
