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
# df.fillna(0,inplace=True)

df['Age']=df['Age'].fillna(df['Age'].mean())

print(df)


# replce a specific column with specific value