# Generated by Django 3.0 on 2020-07-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extest', '0003_auto_20200713_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]