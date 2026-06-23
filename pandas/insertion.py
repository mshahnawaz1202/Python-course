import pandas as pd

data={
    "Name":["Shahnawaz","Hamza","Haider","Mujeeb","ALi"],
    "Age":[19,20,20,21,19],
    "Salary":[50,60,70,80,90],
    "City":["Chiniot","Faisalabad","Chiniot","MULTAN","Chiniot"]
}

df=pd.DataFrame(data)
print("-----------------------------------------------------------------------------------------")
print(df)
print("-----------------------------------------------------------------------------------------")
# insertion with assignment operator
df["Perfromance_Score"]=[4.5,4.3,4,3.9,4]
df["Bonus"]=df["Salary"]*0.1
print(df)
print("-----------------------------------------------------------------------------------------")
df.insert(0,"Emplyee_id",[1,2,3,4,5])
print(df)
