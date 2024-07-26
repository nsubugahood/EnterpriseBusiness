import pandas as pd


data_additional = {
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Children Born to Married Couples": [100000, 102000, 104000, 106000, 108000, 110000, 112000, 114000, 116000]
}

df_additional = pd.DataFrame(data_additional)

print("Smaller Dataset:")
print(df_additional)

df_original = pd.read_csv('marriage_statistics_uganda.csv')


df_original['Divorce Rate'] = df_original['Divorce Rate'].str.rstrip('%').astype('float') / 100.0


df_merged = pd.merge(df_original, df_additional, on='Year', how='left')

print("Merged Dataset:")
print(df_merged)


df_merged.to_csv('merged_marriage_statistics_uganda.csv', index=False)

print("\nMerged dataset saved successfully.")
