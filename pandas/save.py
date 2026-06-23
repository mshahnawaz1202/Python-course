import pandas as pd

data={
    "Name":["Shahnawaz","Ali","Haider"],
    "Age":[19,20,21],
    "City":['Chiniot',"FSD",'Cht']
}

df=pd.DataFrame(data)

print(df)

# df.to_csv("first_data.csv",index=False)


# df.to_excel('output.xlsx', index=False)

df.to_json('output.json',index=False)
