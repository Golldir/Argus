# Generated by Django 5.0.7 on 2024-10-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='center',
            field=models.BooleanField(default=False, verbose_name='Центрирование'),
        ),
    ]