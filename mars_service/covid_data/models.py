from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models


class CovidData(models.Model):
    date = models.DateField()
    death = models.IntegerField(null=True)
    death_increase = models.IntegerField(null=True)
    hospitalized = models.IntegerField(null=True)
    hospitalized_cumulative = models.IntegerField(null=True)
    hospitalized_currently = models.IntegerField(null=True)
    hospitalized_increase = models.IntegerField(null=True)
    in_icu_cumulative = models.IntegerField(null=True)
    in_icu_currently = models.IntegerField(null=True)
    negative = models.IntegerField(null=True)
    negative_increase = models.IntegerField()
    on_ventilator_cumulative = models.IntegerField(null=True)
    on_ventilator_currently = models.IntegerField(null=True)
    pending = models.IntegerField(null=True)
    pos_neg = models.IntegerField(null=True)
    positive = models.IntegerField(null=True)
    positive_increase = models.IntegerField()
    recovered = models.IntegerField(null=True)  # Assume recovered can be nullable
    states = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    total_test_results = models.IntegerField(null=True)
    total_test_results_increase = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.date} - Total Deaths: {self.death}, Total Positive: {self.positive}"
