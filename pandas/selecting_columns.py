import pandas as pd

data={
    "Name":["Shahnawaz","Hamza","Haider","Mujeeb","ALi"],
    "Age":[19,20,20,21,19],
    "Salary":[50,60,70,80,90],
    "City":["Chiniot","Faisalabad","Chiniot","MULTAN","Chiniot"]
}

df=pd.DataFrame(data)
print("------------------SAMPLE DATA FRAME ----------")
print(df)
print("-------------------- Series of data--------------------------------")
name=df["Name"] # selecting one column return series
print(name)

print("-------------------- Data Frame of data--------------------------------")
names=df[["Name","Age","Salary"]] # selecting 2 or more columns returns dataset
print(names)


