from datetime import datetime
from decimal import Decimal
import json
from unicodedata import decimal

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .send_data_to_spread_sheet import send_to_spreadsheet

from .models import *
from django.core.serializers.json import DjangoJSONEncoder

from .shortcuts import check_food_qty_len, message_body


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
        delivery_time_hour = request.POST.get('delivery_time_hour', None)
        delivery_time_min = request.POST.get('delivery_time_min', None)
        delivery_time_ampm = request.POST.get('delivery_time_ampm', None)
        drop_of_location = request.POST.get('drop_of_location', None)
        drop_of_contact = request.POST.get('drop_of_contact', None)
        team = request.POST.get('team', None)
        if '' or None in [email, name, phone_number, delivery_date, delivery_time_hour, delivery_time_min,
                          delivery_time_ampm, drop_of_location, team]:
            messages.add_message(request, messages.WARNING, 'User data')
            return render(request, 'index.html', context)

        user_personal_data = {
            'email': email,
            'name': name,
            'phone_number': phone_number,
            'delivery_time': delivery_time_hour + ':' + delivery_time_min + ' ' + delivery_time_ampm,
            'delivery_date': delivery_date,
            'drop_of_location': drop_of_location,
            'drop_of_contact': drop_of_contact,
            'team': team
        }
        service_charge = (data['total_food_price'] * 20) / 100
        tax_fee = (data['total_food_price'] * Decimal(6.50)) / 100
        total_payable = data['total_food_price'] + service_charge + Decimal(10.00) + tax_fee

        request.session['user_personal_data'] = user_personal_data
        request.session['food_data'] = data['food_data']
        request.session['total_food_price'] = str(data['total_food_price'])
        request.session['service_charge'] = str(service_charge)
        request.session['delivery_fee'] = 10.00
        request.session['tax_fee'] = str(tax_fee)
        request.session['total_payable'] = str(total_payable)
        return redirect('pizza:invoice_payment')

    return render(request, 'index.html', context)


def invoice_payment(request):
    if 'food_data' not in request.session or len(request.session['food_data']) == 0:
        return redirect('pizza:home')
    return render(request, 'invoice.html', {})


def confirm_order(request):
    if request.method == 'POST':
        if 'food_data' not in request.session or len(request.session['food_data']) == 0:
            return redirect('pizza:home')
        #  Todo Send Email start
        mail_subject = "New order at " + str(datetime.ctime)
        message = message_body(request)
        email = EmailMessage(mail_subject, message, to=[settings.CATERING_EMAIL])
        email.content_subtype = "html"
        email.send()
        #  Todo Send Email end

        #  Todo send data to spreadsheet start
        order_data = {"user_personal_data": str(request.session.get('user_personal_data')),
                      "food_data": str(request.session.get('food_data')),
                      "total_food_price": str(request.session.get('total_food_price')),
                      "service_charge": str(request.session.get('service_charge')),
                      "delivery_fee": str(request.session.get('delivery_fee')),
                      "tax_fee": str(request.session.get('tax_fee')),
                      "total_payable": str(request.session.get('total_payable'))
                      }
        send_to_spreadsheet(order_data)
        #  Todo send data to spreadsheet end

        messages.add_message(request, messages.SUCCESS, 'Oder successfully done! We will contact soon.')
        request.session.flush()
        return redirect('pizza:home')

    else:
        request.session.flush()
        return redirect('pizza:home')
