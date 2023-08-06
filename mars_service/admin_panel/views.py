from datetime import datetime


from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from authuser.forms import NewUserForm
from covid_data.models import CovidData
from .forms import NewDataForm  # Import your new form

def admin_panel(request):
    items = CovidData.objects.all()[:30]
    return render(request, 'panel.html', {'items': items})


def create_item(request):
    if request.method == 'POST':
        form = NewDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return JsonResponse({'success': False, 'errors': form.errors})
    return redirect('admin_panel')

def update_item(request, pk):
    item = get_object_or_404(CovidData, pk=pk)
    if request.method == 'POST':
        form = NewDataForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = NewDataForm(instance=item)
    return redirect('admin_panel')

def delete_item(request, pk):
    print("pk is ", pk)
    item = get_object_or_404(CovidData, pk=pk)
    item.delete()
    return redirect('admin_panel')

def get_item_details(request):
    item_id = request.GET.get('item_id')  # Get the item ID from the AJAX request
    if(item_id):
        item = CovidData.objects.get(pk=item_id)
        item_details = {
            'date': item.date,  # Example date
            'hospitalized': item.hospitalized,   # Example hospitalized count
            'death': item.death,            # Example death count
            'positive': item.positive        # Example positive count
        }
        return JsonResponse(item_details)
    else:
        today_date = datetime.today().strftime('%Y-%m-%d')  # Get today's date
        item_details = {
            'date': today_date,
            'hospitalized': 0,
            'death': 0,
            'positive': 0
        }
        return JsonResponse(item_details)