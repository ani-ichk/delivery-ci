def calculate_delivery(subtotal, express=False):
    if not isinstance(subtotal, int) or isinstance(subtotal, bool):
        raise TypeError("subtotal должен быть целым числом")
    if not isinstance(express, bool):
        raise TypeError("express должен быть True или False")
    if subtotal < 0:
        raise ValueError("subtotal не может быть отрицательным")

    if subtotal < 1000:
        cost = 300
    elif subtotal < 5000:
        cost = 150
    else:
        cost = 0

    if express:
        cost += 250
    return cost
