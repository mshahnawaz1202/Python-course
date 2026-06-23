arr=[100,200,300,400,500]

discount=10

final_price=[]

for price in arr:
    final=price-(price*discount)/100
    final_price.append(final)

print(final_price)