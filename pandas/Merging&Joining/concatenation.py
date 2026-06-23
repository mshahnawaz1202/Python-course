import pandas as pd


data1 = {
    "Name": ["Shahnawaz", "Hamza", "Ali", "Usman", "Ahmad", "Hassan", "Bilal"],
    "Age": [19, 20, 22, 21, 23, 25, 24],
    "City": ["Chiniot", "Faisalabad", "Lahore", "Karachi", "Multan", "Islamabad", "Peshawar"]
}


data2 = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard", "Mouse", "Monitor"],
    "Price": [70000, 40000, 25000, 5000, 3000, 1500, 20000],
    "Quantity": [5, 10, 7, 15, 20, 30, 8]
}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("-----------------------------------------------------------------------------------------")
print("First DataFrame:")
print(df1)
print("-----------------------------------------------------------------------------------------")
print("\nSecond DataFrame:")
print(df2)
print("-----------------------------------------------------------------------------------------")
# df_concatenate=pd.concat([df1,df2],axis=0,ignore_index=True)
df_concatenate=pd.concat([df1,df2],axis=1,ignore_index=False)
print(df_concatenate)
print("-----------------------------------------------------------------------------------------")
