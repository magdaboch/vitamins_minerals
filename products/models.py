from django.db import models
from vitamins.models import Vitamin
from minerals.models import Mineral

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(null=True, blank=True)

    product_vitamin = models.ManyToManyField(to=Vitamin, through='ValueVit')
    product_mineral = models.ManyToManyField(to=Mineral, through='ValueMineral')

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

class ValueVit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    vitamin = models.ForeignKey(Vitamin, on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=7, decimal_places=3)

    def __str__(self):
        return f'{self.product} {self.vitamin}'

    class Meta:
        verbose_name = 'Zawartość witaminy w produkcie'
        verbose_name_plural = 'Witaminy w produkcie'

class ValueMineral(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    mineral = models.ForeignKey(Mineral, on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=7, decimal_places=3)

    def __str__(self):
        return f'{self.product} {self.mineral}'

    class Meta:
        verbose_name = 'Zawartość minerału w produkcie'
        verbose_name_plural = 'Minerały w produkcie'

