def fuel_price(litres, price_per_liter):
    discount = int(min(litres, 10)/2) * 5 / 100
    return round((price_per_liter - discount) * litres, 2)
