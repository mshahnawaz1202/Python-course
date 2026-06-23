import pandas as pd


data1 = {
    "ID": [1, 2, 3, 4, 5, 6, 7],
    "Name": ["Shahnawaz", "Hamza", "Ali", "Usman", "Ahmad", "Hassan", "Bilal"],
    "Age": [19, 20, 22, 21, 23, 25, 24],
    "City": ["Chiniot", "Faisalabad", "Lahore", "Karachi", "Multan", "Islamabad", "Peshawar"]
}


data2 = {
    "ID": [1, 2, 3, 44, 5, 6, 9],
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard", "Mouse", "Monitor"],
    "Price": [70000, 40000, 25000, 5000, 3000, 1500, 20000],
    "Quantity": [5, 10, 7, 15, 20, 30, 8]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print("-----------------------------------------------------------------------------------------")
print(df1)
print("-----------------------------------------------------------------------------------------")
print(df2)
# print("-----------------------------------------------------------------------------------------")

merged_df = pd.merge(df1, df2, on="ID",how="inner")

# merged_df = pd.merge(df1, df2, how="cross")
print("---------------------------------------- Merged DataFrame --------------------------------------------------------------------")
# print("Merged DataFrame:")
print(merged_df)
