from django.db import models
from datetime import date

# Create your models here.
class BookNow(models.Model):
    from_city=models.CharField(max_length=50,verbose_name="Where From?")
    to_city=models.CharField(max_length=50,verbose_name="Where To?")
    d_journey=models.DateField(verbose_name="Date of Journey")
    n_persons=models.IntegerField(verbose_name="Number of Persons")