# Generated by Django 3.0.2 on 2020-02-01 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200201_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='valuemineral',
            options={'verbose_name': 'Zawartość minerału w produkcie', 'verbose_name_plural': 'Minerały w produkcie'},
        ),
        migrations.AlterModelOptions(
            name='valuevit',
            options={'verbose_name': 'Zawartość witaminy w produkcie', 'verbose_name_plural': 'Witaminy w produkcie'},
        ),
    ]
