from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv('realistic_dataset.csv')
df_label = df.copy()

# Label Encoding
le = LabelEncoder()
df_label['GenderEncoder'] = le.fit_transform(df_label['Gender'])
df_label['PassedEncoder'] = le.fit_transform(df_label['Passed'])

print('\nLabel Encoded Data\n')

# One Hot Encoding for City
df_encoded = pd.get_dummies(df_label, columns=['City'])

# Convert only the boolean (True/False) dummy columns to 0/1
bool_cols = df_encoded.select_dtypes(include=['bool']).columns
df_encoded[bool_cols] = df_encoded[bool_cols].astype(int)

print('\nOne Hot Encoded Data (City)\n')
print(df_encoded)
