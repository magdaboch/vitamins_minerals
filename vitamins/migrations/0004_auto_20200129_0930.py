# Generated by Django 3.0.2 on 2020-01-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitamins', '0003_vitamin_vitamin_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitamin',
            name='vitamin_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='vitamin',
            name='vitamin_symbol',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
