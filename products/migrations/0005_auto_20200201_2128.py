# Generated by Django 3.0.2 on 2020-02-01 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200201_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valuemineral',
            name='value',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
