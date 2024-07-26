import pandas as pd

df = pd.read_csv('marriage_statistics_uganda.csv')

print("Initial Dataset:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())

df['Divorce Rate'] = df['Divorce Rate'].str.rstrip('%').astype('float') / 100.0


df.fillna(df.mean(), inplace=True)

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

df['Total Marriages'] = pd.to_numeric(df['Total Marriages'], errors='coerce')
df['Urban Marriages'] = pd.to_numeric(df['Urban Marriages'], errors='coerce')
df['Rural Marriages'] = pd.to_numeric(df['Rural Marriages'], errors='coerce')
df['Population'] = pd.to_numeric(df['Population'], errors='coerce')


print("\nData Types after Conversion:")
print(df[['Total Marriages', 'Urban Marriages', 'Rural Marriages', 'Population']].dtypes)

print("\nCleaned Dataset:")
print(df.head())


df.to_csv('cleaned_marriage_statistics_uganda.csv', index=False)

print("\nCleaned dataset saved successfully.")
