from django.db import models
from areas.models import Areas
# Create your models here.
class Consumo(models.Model):
    id = models.AutoField(primary_key=True)
    consumo_r = models.DecimalField(max_digits=15, decimal_places=2)
    consumo_s = models.DecimalField(max_digits=15, decimal_places=2)
    consumo_t = models.DecimalField(max_digits=15, decimal_places=2)
    consumo_total = models.DecimalField(max_digits=15, decimal_places=2)
    ts = models.DateTimeField(auto_now_add=True)
    area = models.ForeignKey(Areas, blank=True, null=True, on_delete=models.DO_NOTHING)
