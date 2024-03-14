def ogprice(price,percentage):
    discount=price *(percentage/100)
    ogprice =price - discount
    return round(ogprice)



    
    
print(ogprice(1500,50))
print(ogprice(89,20))
print(ogprice(100,75))