# Generated by Django 3.0.2 on 2020-01-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0002_auto_20200128_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='mineral_symbol',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
