from django.db import models

# Create your models here.
class Vitamin(models.Model):
    UNIT_TYPE = (
        ('mg', 'miligram'),
        ('μg', 'mikrogram'),
    )
    vitamin_name = models.CharField(max_length=150, null=True, blank=True)
    vitamin_symbol = models.CharField(max_length=100, null=True, blank=True)
    vitamin_unit = models.CharField(max_length=10, choices=UNIT_TYPE)
    vitamin_recomended_consuption = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return f'{self.vitamin_name} [{self.vitamin_unit}]'

    class Meta:
        verbose_name = 'Witamina'
        verbose_name_plural = 'Witaminy'