# Generated by Django 5.0.7 on 2024-10-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_sensor_center'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='line_breaks',
            field=models.BooleanField(default=False, verbose_name='Перенос строки'),
        ),
    ]
