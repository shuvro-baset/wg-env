from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def home(request):
    dessert_ins = Dessert.objects.all().order_by('id')
    salad_dressing_ins = SaladDressing.objects.all().order_by('id')
    salad_ins = Salad.objects.all().order_by('id')
    wing_sauce_ins = WingSauce.objects.all().order_by('id')
    wing_ins = Wing.objects.all().order_by('id')
    bread_ins = Bread.objects.all().order_by('id')
    gluten_cauliflower_ins = GlutenCauliflower.objects.all().order_by('id')
    pizza_ins = Pizza.objects.all().order_by('id')
    context = {
        'desserts': dessert_ins,
        'salad_dressings': salad_dressing_ins,
        'salads': salad_ins,
        'wing_sauces': wing_sauce_ins,
        'wings': wing_ins,
        'breads': bread_ins,
        'gluten_cauliflowers': gluten_cauliflower_ins,
        'pizzas': pizza_ins,
    }

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
            messages.add_message(request, messages.WARNING, 'Please select a pizza and quantity first.')
            return render(request, 'index.html', context)
        # elif pizzas_length != pizzas_qty_length:
        #     messages.add_message(request, messages.WARNING, 'Pizza Quantity not given properly!')
        #     return render(request, 'index.html', context)

        print(request.POST)

    return render(request, 'index.html', context)
