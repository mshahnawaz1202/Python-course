import pandas as pd

data={
    "Name":["Shahnawaz","Hamza","Haider","Mujeeb","ALi"],
    "Age":[19,20,None,21,19],
    "Salary":[50,60,70,80,None],
    "City":["Chiniot","Faisalabad","Chiniot","MULTAN","Chiniot"]
}

df=pd.DataFrame(data)

print("-----------------------------------------------------------------------------------------")
print(df)
print("---------------------------------Sorted--------------------------------------------------------")
# df.sort_values(by='Name',ascending=True,inplace=True)
# print(df)

# print("-----------------------------------------------------------------------------------------")
df.sort_values(by=['Name','Age'],ascending=[True,False],inplace=True)
print(df)



