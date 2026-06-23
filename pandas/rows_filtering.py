import pandas as pd

data={
    "Name":["Shahnawaz","Hamza","Haider","Mujeeb","ALi"],
    "Age":[19,20,20,21,18],
    "Salary":[75,78,70,80,90],
    "City":["Chiniot","Faisalabad","Chiniot","MULTAN","Chiniot"]
}

df=pd.DataFrame(data)

filter_rows=df[df["Salary"]>60]
print("High salary employees : ")
print(filter_rows)
print("High salary employees with high age ")
double_condition_filetering=df[(df['Salary']>60)& (df["Age"]>=19)]

print(double_condition_filetering)