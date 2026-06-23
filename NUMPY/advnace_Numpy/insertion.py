import numpy as np

arr=np.array([10,20,30,40,50])
print("------------1D--------------")
print(arr)

new_arr=np.insert(arr,2,33)
print(new_arr)

print("------------2D--------------")

# insertion in 2d
arr_2d=np.array([[1,2],[3,4]])
print(arr_2d)

new_arr_2d=np.insert(arr_2d,1,[5,6],axis=0) # row wise insertion
print(f"Row wise insertion in 2D:\n{new_arr_2d}")
new_arr1_2d=np.insert(arr_2d,1,[8,9],axis=1) # column wise insertion
print(f"Row wise insertion in 2D:\n{new_arr1_2d}")