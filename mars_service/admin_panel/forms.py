from django import forms
from covid_data.models import CovidData  # Import your model

class NewDataForm(forms.ModelForm):
    class Meta:
        model = CovidData
        fields = ('date', 'hospitalized', 'death', 'positive')