# Generated by Django 3.0.6 on 2020-06-25 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyTraker', '0013_timers_totalhours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timers',
            name='totalhours',
            field=models.DecimalField(decimal_places=5, max_digits=5),
        ),
    ]
