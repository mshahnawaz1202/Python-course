"""
np.split() ->> equal

np.hsplit() ->> horizontally
np.vsplit() ->> vertically

can through errors on size 
"""

import numpy as np

arr1=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.split(arr1,2))


print(np.hsplit(arr1,2))


