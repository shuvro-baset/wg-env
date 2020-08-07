def check_food_qty_len(request):
    gluten_cauliflower = request.POST.getlist('gluten_cauliflower', None)
    gluten_cauliflower_qty = request.POST.getlist('gluten_cauliflower_qty', None)
    if len(gluten_cauliflower) != 0:
        if len(gluten_cauliflower) != len(gluten_cauliflower_qty):
            return False, 'Gluten Free and Cauliflower Crust Quantity not given properly!'

    wings_sauce = request.POST.getlist('wings_sauce', None)
    wings_sauce_qty = request.POST.getlist('wings_sauce_qty', None)
    if len(wings_sauce) != 0:
        if len(wings_sauce) != len(wings_sauce_qty):
            return False, 'Wings Sauces Quantity not given properly!'

    salad = request.POST.getlist('salad', None)
    salad_qty = request.POST.getlist('salad_qty', None)
    if len(salad) != 0:
        if len(salad) != len(salad_qty):
            return False, 'Salads Quantity not given properly!'

    salad_dressing = request.POST.getlist('salad_dressing', None)
    salad_dressing_qty = request.POST.getlist('salad_dressing_qty', None)
    if len(salad_dressing) != 0:
        if len(salad_dressing) != len(salad_dressing_qty):
            return False, 'Salad Dressings Quantity not given properly!'

    dessert = request.POST.getlist('dessert', None)
    dessert_qty = request.POST.getlist('dessert_qty', None)
    if len(dessert) != 0:
        if len(dessert) != len(dessert_qty):
            return False, 'Desserts Quantity not given properly!'

    bread = request.POST.getlist('bread', None)
    bread_qty = request.POST.getlist('bread_qty', None)
    if len(bread) != 0:
        if len(bread) != len(bread_qty):
            return False, 'Breads Quantity not given properly!'

    wing = request.POST.getlist('wing', None)
    wing_qty = request.POST.getlist('wing_qty', None)
    if len(wing) != 0:
        if len(wing) != len(wing_qty):
            return False, 'Wings Quantity not given properly!'

    return True, ''
