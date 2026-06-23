import numpy as np

arr=np.array([1,2,3,4,np.inf,6,-np.inf])

print(np.isinf(arr))

cleaned_arr=np.nan_to_num(arr,posinf=100,neginf=-100)
print(cleaned_arr)