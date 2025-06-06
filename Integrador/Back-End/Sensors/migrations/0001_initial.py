# Generated by Django 5.2.1 on 2025-05-23 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sig', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('ni', models.CharField(max_length=256)),
                ('task', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('sensors', models.CharField(choices=[('Temp', 'Temperature - °C'), ('Lumi', 'Luminosity -lux'), ('Cont', 'Counter - num'), ('Humi', 'Humidity - %')], max_length=4)),
                ('mac_address', models.CharField(max_length=256)),
                ('unit_of_measure', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
                ('latitude', models.FloatField()),
                ('longitude', models.CharField()),
                ('status', models.BooleanField(default=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Historic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('timestamp', models.IntegerField()),
                ('ambiance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sensors.ambience')),
                ('sensors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sensors.sensors')),
            ],
        ),
    ]
