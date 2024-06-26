# Generated by Django 5.0.5 on 2024-05-06 18:35

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(max_length=100)),
                ('car_type', models.CharField(
                    choices=[
                        ('SEDAN', 'Sedan'),
                        ('SUV', 'SUV'),
                        ('WAGON', 'Wagon'),
                        ('COUPE', 'Coupe'),
                        ('CONVERTIBLE', 'Convertible')
                    ],
                    default='SUV',
                    max_length=11
                )),
                ('year', models.IntegerField(
                    default=2023,
                    validators=[
                        django.core.validators.MaxValueValidator(2023),
                        django.core.validators.MinValueValidator(2015)
                    ]
                )),
                ('engine_type', models.CharField(max_length=20)),
                ('transmission_type', models.CharField(max_length=10)),
                ('car_make', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='djangoapp.carmake'
                )),
            ],
        ),
    ]
