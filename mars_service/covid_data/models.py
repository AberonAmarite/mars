from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models


class CovidData(models.Model):
    date = models.DateField()
    death = models.IntegerField(null=True)
    hospitalized = models.IntegerField(null=True)
    positive = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.date} - Total Deaths: {self.death}, Total Positive: {self.positive}"
