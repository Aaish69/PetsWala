# Generated by Django 3.2.9 on 2022-04-11 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_request_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='rescue_note',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('TO DO', 'TO DO'), ('In Progress', 'In Progress'), ('Blocked', 'Blocked'), ('Complete', 'Complete')], default='TO DO', max_length=20),
        ),
    ]
