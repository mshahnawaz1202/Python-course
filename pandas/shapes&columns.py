import pandas as pd

data={
    "Name":["Shahnawaz","Hamza","Haider","Mujeeb","ALi"],
    "Age":[19,20,20,21,19],
    "Salary":[50,60,70,80,90],
    "City":["Chiniot","Faisalabad","Chiniot","MULTAN","Chiniot"]
}

df=pd.DataFrame(data)

print(df)

print(f"Shape : {df.shape}")
print(f"Columns Names : {df.columns}")