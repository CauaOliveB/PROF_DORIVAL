# Generated by Django 5.1.7 on 2025-03-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER_JWT', '0005_alter_userabs_endereco_alter_userabs_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userabs',
            name='idade',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userabs',
            name='telefone',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
