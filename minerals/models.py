from django.db import models

# Create your models here.
class Mineral(models.Model):
    UNIT_TYPE = (
        ('mg', 'miligram'),
        ('μg', 'mikrogram'),
    )
    mineral_name = models.CharField(max_length=150)
    mineral_symbol = models.CharField(max_length=50)
    mineral_unit = models.CharField(max_length=10, choices=UNIT_TYPE)
    mineral_recomended_consuption = models.DecimalField(max_digits=7, decimal_places=3)

    def __str__(self):
        return f'{self.mineral_name} [{self.mineral_unit}]'

    class Meta:
        verbose_name = 'Minerał'
        verbose_name_plural = 'Minerały'