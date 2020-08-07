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
        team = request.POST.get('team', None)
        pizzas = request.POST.getlist('pizzas', None)
        pizzas_qty = request.POST.getlist('pizzas_qty', None)
        pizzas_length = len(pizzas)
        pizzas_qty_length = len(pizzas_qty)
        if pizzas_length == 0:
            messages.add_message(request, messages.WARNING, 'Please select a pizza first.')
            return render(request, 'index.html')
        # elif pizzas_length != pizzas_qty_length:
        #     messages.add_message(request, messages.WARNING, 'Pizza Quantity not given properly!')
        #     return render(request, 'index.html')

        print(pizzas_qty, len(pizzas))
    return render(request, 'index.html')
