import pandas as pd

df=pd.read_csv("sales_data_sample.csv",encoding="latin1")
# df=pd.read_json("sample_Data.json")

# print(df)

print("First 10 rows")
print(df.head(10)) # display first n rows if no value inside head  it will show default first 5 rows



print("last 10 rows")

print(df.tail(10)) # display last n rows if no value inside head  it will show default last 5 rows