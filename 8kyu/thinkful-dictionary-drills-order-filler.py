def fillable(stock, merch, n):
    return stock[merch] >= n if merch in stock else False
