# Generated by Django 3.0.6 on 2020-06-16 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PyTraker', '0009_auto_20200616_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timers',
            name='projectID',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='PyTraker.Projects'),
        ),
    ]
