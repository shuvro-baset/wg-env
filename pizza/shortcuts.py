from unicodedata import decimal

from django.db.models import Sum

from .models import *


def check_food_qty_len(request):
    total_food_price = 0
    data = {}
    food_data = []
    pizzas = request.POST.getlist('pizzas', None)
    if len(pizzas) == 0:
        return False, 'Please select at least one pizza and quantity first.', data
    else:
        pizza_ins = Pizza.objects.filter(id__in=pizzas)
        for pizza in pizza_ins:
            temp_data = {}
            pizza_qty = 'pizzas_qty_' + str(pizza.id)
            input_pizza_qty = request.POST.get(pizza_qty, None)
            if input_pizza_qty is None or input_pizza_qty == '':
                return False, 'Pizza Quantity not given properly!', data
            temp_data['name'] = pizza.name
            temp_data['total_price'] = str(pizza.price * decimal(input_pizza_qty))
            temp_data['qty'] = input_pizza_qty
            food_data.append(temp_data)
            total_food_price += pizza.price * decimal(input_pizza_qty)

    gluten_cauliflower = request.POST.getlist('gluten_cauliflower', None)
    if len(gluten_cauliflower) != 0:
        gluten_cauliflower_ins = GlutenCauliflower.objects.filter(id__in=gluten_cauliflower)
        for gluten_cauliflower in gluten_cauliflower_ins:
            temp_data = {}
            gluten_cauliflower_qty = 'gluten_cauliflower_qty_' + str(gluten_cauliflower.id)
            input_gluten_cauliflower_qty = request.POST.get(gluten_cauliflower_qty, None)
            if input_gluten_cauliflower_qty is None or input_gluten_cauliflower_qty == '':
                return False, 'Gluten Free and Cauliflower Crust Quantity not given properly!', data
            temp_data['name'] = gluten_cauliflower.name
            temp_data['total_price'] = str(gluten_cauliflower.price * decimal(input_gluten_cauliflower_qty))
            temp_data['qty'] = input_gluten_cauliflower_qty
            food_data.append(temp_data)
            total_food_price += gluten_cauliflower.price * decimal(input_gluten_cauliflower_qty)

    # gluten_cauliflower_total_ins = GlutenCauliflower.objects.filter(id__in=pizzas).aggregate(Sum('price'))[
    #         'price__sum']
    #     total_price += gluten_cauliflower_total_ins

    wings_sauce = request.POST.getlist('wings_sauce', None)
    if len(wings_sauce) != 0:
        wings_sauce_ins = WingSauce.objects.filter(id__in=wings_sauce)
        for wings_sauce_data in wings_sauce_ins:
            temp_data = {}
            wings_sauce_qty = 'wings_sauce_qty_' + str(wings_sauce_data.id)
            input_wings_sauce_qty = request.POST.get(wings_sauce_qty, None)
            special_request = request.POST.get('wings_sauce_special_request', None)
            if input_wings_sauce_qty is None or input_wings_sauce_qty == '':
                return False, 'Wings Sauces Quantity not given properly!', data
            temp_data['name'] = wings_sauce_data.name
            temp_data['total_price'] = str(wings_sauce_data.price * decimal(input_wings_sauce_qty))
            temp_data['qty'] = input_wings_sauce_qty
            temp_data['special_request'] = special_request
            food_data.append(temp_data)
            total_food_price += wings_sauce_data.price * decimal(input_wings_sauce_qty)

    salad = request.POST.getlist('salad', None)
    if len(salad) != 0:
        salad_ins = Salad.objects.filter(id__in=salad)
        for salad_data in salad_ins:
            temp_data = {}
            salad_qty = 'salad_qty_' + str(salad_data.id)
            input_salad_qty = request.POST.get(salad_qty, None)
            special_request = request.POST.get('salad_special_request', None)
            if input_salad_qty is None or input_salad_qty == '':
                return False, 'Salads Quantity not given properly!', data
            temp_data['name'] = salad_data.name
            temp_data['total_price'] = str(salad_data.price * decimal(input_salad_qty))
            temp_data['qty'] = input_salad_qty
            temp_data['special_request'] = special_request
            food_data.append(temp_data)
            total_food_price += salad_data.price * decimal(input_salad_qty)

    salad_dressing = request.POST.getlist('salad_dressing', None)
    salad_dressing_qty = request.POST.getlist('salad_dressing_qty', None)
    if len(salad_dressing) != 0:
        salad_dressing_ins = SaladDressing.objects.filter(id__in=salad_dressing)
        for salad_dressing_data in salad_dressing_ins:
            temp_data = {}
            salad_dressing_qty = 'salad_dressing_qty_' + str(salad_dressing_data.id)
            input_salad_dressing_qty = request.POST.get(salad_dressing_qty, None)
            if input_salad_dressing_qty is None or input_salad_dressing_qty == '':
                return False, 'Salad Dressings Quantity not given properly!', data
            temp_data['name'] = salad_dressing_data.name
            temp_data['total_price'] = str(salad_dressing_data.price * decimal(input_salad_dressing_qty))
            temp_data['qty'] = input_salad_dressing_qty
            food_data.append(temp_data)
            total_food_price += salad_dressing_data.price * decimal(input_salad_dressing_qty)

    dessert = request.POST.getlist('dessert', None)
    dessert_qty = request.POST.getlist('dessert_qty', None)
    if len(dessert) != 0:
        dessert_ins = Dessert.objects.filter(id__in=dessert)
        for dessert_data in dessert_ins:
            temp_data = {}
            dessert_qty = 'dessert_qty_' + str(dessert_data.id)
            input_dessert_qty = request.POST.get(dessert_qty, None)
            special_request = request.POST.get('dessert_special_request', None)
            if input_dessert_qty is None or input_dessert_qty == '':
                return False, 'Desserts Quantity not given properly!', data
            temp_data['name'] = dessert_data.name
            temp_data['total_price'] = str(dessert_data.price * decimal(input_dessert_qty))
            temp_data['qty'] = input_dessert_qty
            temp_data['special_request'] = special_request
            food_data.append(temp_data)
            total_food_price += dessert_data.price * decimal(input_dessert_qty)

    bread = request.POST.getlist('bread', None)
    if len(bread) != 0:
        bread_ins = Bread.objects.filter(id__in=bread)
        for bread_data in bread_ins:
            temp_data = {}
            bread_qty = 'bread_qty_' + str(bread_data.id)
            input_bread_qty = request.POST.get(bread_qty, None)
            if input_bread_qty is None or input_bread_qty == '':
                return False, 'Breads Quantity not given properly!', data
            temp_data['name'] = bread_data.name
            temp_data['total_price'] = str(bread_data.price * decimal(input_bread_qty))
            temp_data['qty'] = input_bread_qty
            food_data.append(temp_data)
            total_food_price += bread_data.price * decimal(input_bread_qty)

    wing = request.POST.getlist('wing', None)
    wing_qty = request.POST.getlist('wing_qty', None)
    if len(wing) != 0:
        wing_ins = Wing.objects.filter(id__in=wing)
        for wing_data in wing_ins:
            temp_data = {}
            wing_qty = 'wing_qty_' + str(wing_data.id)
            input_wing_qty = request.POST.get(wing_qty, None)
            if input_wing_qty is None or input_wing_qty == '':
                return False, 'Wings Quantity not given properly!', data
            temp_data['name'] = wing_data.name
            temp_data['total_price'] = str(wing_data.price * decimal(input_wing_qty))
            temp_data['qty'] = input_wing_qty
            food_data.append(temp_data)
            total_food_price += wing_data.price * decimal(input_wing_qty)

    # print('total price: ', total_price)
    # print('food data: ', food_data)
    data = {
        'food_data': food_data,
        'total_food_price': total_food_price
    }

    return True, '', data
