import numpy as np

arr=np.array([1,2,3,4,np.nan,6,np.nan])

cleaned_arr=np.nan_to_num(arr)
print(cleaned_arr)

cleaned_arr1=np.nan_to_num(arr,nan=45)
print(cleaned_arr1)