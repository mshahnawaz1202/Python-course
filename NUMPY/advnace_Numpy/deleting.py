import numpy as np
# arr1=np.array([1,2,3,4,5,6,7,8,9])
# print(arr1)

# new_arr=np.delete(arr1,3,axis=None)
# print(new_arr)

#2D
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d)
print("----------row wise----------------------------")
new_2d=np.delete(arr_2d,0,axis=0)
print(new_2d)
print("----------column wise----------------------------")
new_2d_1=np.delete(arr_2d,0,axis=1)
print(new_2d_1)