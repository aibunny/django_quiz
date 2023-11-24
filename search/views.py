from django.shortcuts import render
from . models import *
from . forms import *


def search_passengers(request):
    form = PassengerSearchForm(request.GET)
    passengers =Passengers.objects.all()
    
    if form.is_valid():
        #Apply filter based on name in the form data
        name = form.cleaned_data.get('name')
        
        if name:
            passengers = passengers.filter(name__icontains=name)
            
        return render(request, 'search_results.html', {'form': form, 'passengers': passengers})