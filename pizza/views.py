from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        name = request.POST.get('name', None)
        phone_number = request.POST.get('phone_number', None)
        delivery_date = request.POST.get('delivery_date', None)
        delivery_time = request.POST.get('delivery_time', None)
        drop_of_location = request.POST.get('drop_of_location', None)
        team = request.POST.get('team')
        pizzas = request.POST.getlist('vehicle3', None)
        pizzas_length = len(pizzas)
        if pizzas == 0:
            messages.add_message(request, messages.warning, 'Please select a pizza first.')
            return render(request, 'index.html')

        print(email, name, len(pizzas))
    return render(request, 'index.html')
