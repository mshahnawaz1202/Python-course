import numpy as np

array_default=np.zeros(4)

print(array_default)

array_default_2d=np.zeros((3,4))
print(array_default_2d)
print("\n")

# array_default_1d_one=np.ones(3)
# print(array_default_1d_one)

array_default_2d_one=np.ones((4,5))
print(array_default_2d_one)

# np.full((shape),value)
full_array=np.full((2,3),7)

print(full_array)