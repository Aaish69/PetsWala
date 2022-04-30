# Generated by Django 3.2.9 on 2022-04-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_address_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescueservices',
            name='address',
            field=models.CharField(default='lums in gate', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='address',
            field=models.CharField(default='lums', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vet',
            name='address',
            field=models.CharField(default='lums', max_length=100),
            preserve_default=False,
        ),
    ]
