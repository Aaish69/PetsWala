# Generated by Django 3.2.9 on 2022-04-20 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_merge_0021_vet_appointment_0023_auto_20220411_0612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'ordering': ['-update_at', '-created_at']},
        ),
    ]