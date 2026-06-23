import pandas as pd

data={
    "Name":["Shahnawaz","Hamza","Haider","Mujeeb","ALi"],
    "Age":[19,20,None,21,19],
    "Salary":[50,60,70,80,None],
    "City":["Chiniot","Faisalabad",None,"MULTAN","Chiniot"]
}

df=pd.DataFrame(data)

print("-----------------------------------------------------------------------------------------")
print(df)


print("-----------------------------------------------------------------------------------------")
df.dropna(inplace=True)
print(df)