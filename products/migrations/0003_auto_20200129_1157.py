# Generated by Django 3.0.2 on 2020-01-29 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0003_mineral_mineral_symbol'),
        ('products', '0002_auto_20200129_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValueMineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=3, max_digits=6)),
                ('mineral', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='minerals.Mineral')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_mineral',
            field=models.ManyToManyField(through='products.ValueMineral', to='minerals.Mineral'),
        ),
    ]
