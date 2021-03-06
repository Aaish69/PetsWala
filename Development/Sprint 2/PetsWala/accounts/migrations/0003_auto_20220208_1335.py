# Generated by Django 3.2.8 on 2022-02-08 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='RescueService',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('is_approved', models.BooleanField(default=False)),
                ('company_info', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('is_approved', models.BooleanField(default=False)),
                ('company_info', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_rescue_service',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_serviceprovider',
            field=models.BooleanField(default=False),
        ),
    ]
