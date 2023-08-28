# Generated by Django 4.2.4 on 2023-08-28 12:39

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='Дата')),
                ('temperature', models.IntegerField(validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)], verbose_name='Температура (°C)')),
                ('humidity', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Влажность (%)')),
                ('pressure', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(700), django.core.validators.MaxValueValidator(800)], verbose_name='Атмосферное давление (мм.рт.ст.)')),
                ('wind_direction', models.CharField(max_length=5, verbose_name='Направление ветра')),
                ('wind_speed', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Скорость ветра (м/с)')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sights.sights', verbose_name='Примечательное место')),
            ],
            options={
                'verbose_name': 'Сводка погоды',
                'verbose_name_plural': 'Сводки погоды',
            },
        ),
    ]
