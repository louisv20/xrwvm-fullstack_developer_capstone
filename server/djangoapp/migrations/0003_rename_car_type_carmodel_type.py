# Generated by Django 5.0.5 on 2024-05-07 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_remove_carmodel_engine_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='car_type',
            new_name='type',
        ),
    ]
