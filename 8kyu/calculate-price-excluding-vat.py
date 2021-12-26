def excluding_vat_price(price):
    return round((price*100/115), 2) if price != None else -1
