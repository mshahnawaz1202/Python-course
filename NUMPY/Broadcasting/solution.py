import numpy as np

price=np.array([100,200,300,400,500])
discount=10
final_price=price-(price*discount/100)

print(final_price)