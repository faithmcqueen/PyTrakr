# Generated by Django 3.0.7 on 2020-06-13 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PyTraker', '0006_auto_20200611_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tasks',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
