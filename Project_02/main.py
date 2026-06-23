import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------------------

df=pd.read_csv('employees_large.csv')
# print(df)

print("------------------- Info of Dataset --------------------")
print(df.info())



# print("------------ Checking Null values -----------------------------")
# print(df.isnull())


#----------------- converting null numeric values to its column avg values --------------
df.interpolate(method='linear',axis=0,inplace=True)

# print(df.dropna())
# print("------------------- Info of Dataset --------------------")
# print(df.info())

#------------------- remove remaining that cannot be converted -------------------
df.dropna(axis=0,inplace=True)
print("------------------- Info of Dataset --------------------")
print(df.info())

#---------------------------------------------------
name=df['Department'].to_numpy()
experience=df['Experience'].to_numpy()

plt.bar(name,experience,color='red')
plt.legend()
plt.xlabel('Department')
plt.ylabel('Experience')
plt.title('Experience in different deparments')
plt.grid()
plt.show()


#------------------------------------------------------------------------------








