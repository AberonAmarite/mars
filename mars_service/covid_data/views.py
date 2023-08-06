from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
import json
from covid_data.models import CovidData

def index(request): #HttpRequest
    if not request.user.is_authenticated:
        return redirect('login')
    covid_data_objects = CovidData.objects.all()[:30]  # Retrieve the first 30 objects
    data = {}

    for entry in covid_data_objects:
        data[entry.date.strftime('%Y-%m-%d')] = {
            'death': entry.death,
            'hospitalized': entry.hospitalized
        }

    json_data = json.dumps(data)
    return render(request, 'index.html', {'title': 'Bitle', 'data': json_data})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
