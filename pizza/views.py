import json

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.serializers.json import DjangoJSONEncoder

from .shortcuts import check_food_qty_len


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
        # check post-values
        is_ok, error_message, data = check_food_qty_len(request)
        if is_ok is False:
            messages.add_message(request, messages.WARNING, error_message)
            return render(request, 'index.html', context)

        email = request.POST.get('email', None)
        name = request.POST.get('name', None)
        phone_number = request.POST.get('phone_number', None)
        delivery_date = request.POST.get('delivery_date', None)
        delivery_time = request.POST.get('delivery_time', None)
        drop_of_location = request.POST.get('drop_of_location', None)
        team = request.POST.get('team', None)
        user_personal_data = {
            'email': email,
            'name': name,
            'phone_number': phone_number,
            'delivery_time': delivery_time,
            'delivery_date': delivery_date,
            'drop_of_location': drop_of_location,
            'team': team
        }

        # pizzas = request.POST.getlist('pizzas', None)
        # pizzas_qty = request.POST.getlist('pizzas_qty', None)
        # if len(pizzas) == 0:
        #     messages.add_message(request, messages.WARNING, 'Please select at least one pizza and quantity first.')
        #     return render(request, 'index.html', context)
        # elif len(pizzas) != len(pizzas_qty):
        #     messages.add_message(request, messages.WARNING, 'Pizza Quantity not given properly!')
        #     return render(request, 'index.html', context)

        # print(request.POST)

        request.session['user_personal_data'] = user_personal_data
        request.session['food_data'] = data['food_data']
        request.session['total_food_price'] = data['total_food_price']
        # print(json.dumps(data, cls=DjangoJSONEncoder), user_personal_data)
        return redirect('pizza:invoice_payment')

    return render(request, 'index.html', context)


def invoice_payment(request):
    return render(request, 'invoice.html', {})
