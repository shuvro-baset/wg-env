from unicodedata import decimal

from django.db.models import Sum

from .models import *


def check_food_qty_len(request):
    total_price = 0
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
            temp_data['total_price'] = pizza.price * decimal(input_pizza_qty)
            temp_data['qty'] = input_pizza_qty
            food_data.append(temp_data)
            # total_price += pizza.price * decimal(input_pizza_qty)

    gluten_cauliflower = request.POST.getlist('gluten_cauliflower', None)
    if len(gluten_cauliflower) != 0:
        gluten_cauliflower_ins = GlutenCauliflower.objects.filter(id__in=gluten_cauliflower)
        for gluten_cauliflower in gluten_cauliflower_ins:
            temp_data = {}
            gluten_cauliflower_qty_ = 'gluten_cauliflower_qty_' + str(gluten_cauliflower.id)
            input_gluten_cauliflower_qty = request.POST.get(gluten_cauliflower_qty_, None)
            if input_gluten_cauliflower_qty is None and input_gluten_cauliflower_qty == '':
                return False, 'Gluten Free and Cauliflower Crust Quantity not given properly!', data
            temp_data['name'] = gluten_cauliflower.name
            temp_data['total_price'] = gluten_cauliflower.price * decimal(input_gluten_cauliflower_qty)
            temp_data['qty'] = input_gluten_cauliflower_qty
            food_data.append(temp_data)
            # total_price += gluten_cauliflower.price * decimal(input_gluten_cauliflower_qty)

    # gluten_cauliflower_total_ins = GlutenCauliflower.objects.filter(id__in=pizzas).aggregate(Sum('price'))[
    #         'price__sum']
    #     total_price += gluten_cauliflower_total_ins

    wings_sauce = request.POST.getlist('wings_sauce', None)
    wings_sauce_qty = request.POST.getlist('wings_sauce_qty', None)
    if len(wings_sauce) != 0:
        if len(wings_sauce) != len(wings_sauce_qty):
            return False, 'Wings Sauces Quantity not given properly!', data

    salad = request.POST.getlist('salad', None)
    salad_qty = request.POST.getlist('salad_qty', None)
    if len(salad) != 0:
        if len(salad) != len(salad_qty):
            return False, 'Salads Quantity not given properly!', data

    salad_dressing = request.POST.getlist('salad_dressing', None)
    salad_dressing_qty = request.POST.getlist('salad_dressing_qty', None)
    if len(salad_dressing) != 0:
        if len(salad_dressing) != len(salad_dressing_qty):
            return False, 'Salad Dressings Quantity not given properly!', data

    dessert = request.POST.getlist('dessert', None)
    dessert_qty = request.POST.getlist('dessert_qty', None)
    if len(dessert) != 0:
        if len(dessert) != len(dessert_qty):
            return False, 'Desserts Quantity not given properly!', data

    bread = request.POST.getlist('bread', None)
    bread_qty = request.POST.getlist('bread_qty', None)
    if len(bread) != 0:
        if len(bread) != len(bread_qty):
            return False, 'Breads Quantity not given properly!', data

    wing = request.POST.getlist('wing', None)
    wing_qty = request.POST.getlist('wing_qty', None)
    if len(wing) != 0:
        if len(wing) != len(wing_qty):
            return False, 'Wings Quantity not given properly!', data

    print('total price: ', total_price)
    print('food data: ', food_data)
    data = {
        'food_data': food_data,
        'total_price': total_price
    }

    return True, '', data
