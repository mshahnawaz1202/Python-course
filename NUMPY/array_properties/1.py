import numpy as np

arr_2d=np.array([[1,2,3]
                ,[4,5,6]])

arr=np.array([[[1,2],[3,4],[5,6]]])
# shape
# print(arr_2d.shape)

# #size

# print(arr.size)

# # no of dimensions

# print(arr_2d.ndim)
# print(arr.ndim)


# type of data 

print(arr.dtype)
# canfing type of Data
float_arr=arr.astype(float)

print(float_arr)
print(float_arr.dtype)


