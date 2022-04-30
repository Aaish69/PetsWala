# Generated by Django 3.2.9 on 2022-04-20 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_alter_request_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m1', models.BooleanField(default=False)),
                ('m2', models.BooleanField(default=False)),
                ('m3', models.BooleanField(default=False)),
                ('m4', models.BooleanField(default=False)),
                ('t1', models.BooleanField(default=False)),
                ('t2', models.BooleanField(default=False)),
                ('t3', models.BooleanField(default=False)),
                ('t4', models.BooleanField(default=False)),
                ('w1', models.BooleanField(default=False)),
                ('w2', models.BooleanField(default=False)),
                ('w3', models.BooleanField(default=False)),
                ('w4', models.BooleanField(default=False)),
                ('th1', models.BooleanField(default=False)),
                ('th2', models.BooleanField(default=False)),
                ('th3', models.BooleanField(default=False)),
                ('th4', models.BooleanField(default=False)),
                ('f1', models.BooleanField(default=False)),
                ('f2', models.BooleanField(default=False)),
                ('f3', models.BooleanField(default=False)),
                ('f4', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.serviceprovider')),
            ],
        ),
    ]
