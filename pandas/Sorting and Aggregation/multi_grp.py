import pandas as pd

data={
    "Name":["Zaid","Hamza","Haider","Mujeeb","ALi"],
    "Age":[19,20,22,20,19],
    "Salary":[79000,60000,75000,65000,72000],
    "City":["Pensara","Faisalabad","Chiniot","MULTAN","Chiniot"]
}

df=pd.DataFrame(data)

print("-----------------------------------------------------------------------------------------")
print(df)
print("-----------------------------------------------------------------------------------------")

grouped=df.groupby(["Age","City"])['Salary'].sum()
print(grouped)
print("-----------------------------------------------------------------------------------------")
