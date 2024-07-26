import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np


df = pd.read_csv('merged_marriage_statistics_uganda.csv')

print("Merged Dataset:")
print(df.head())


desc_stats = df.describe()
print("Descriptive Statistics:")
print(desc_stats)

plt.figure(figsize=(14, 8))

plt.subplot(2, 2, 1)
sns.lineplot(data=df, x='Year', y='Total Marriages', marker='o')
plt.title('Total Marriages Over the Years')


plt.subplot(2, 2, 2)
sns.lineplot(data=df, x='Year', y='Children Born to Married Couples', marker='o')
plt.title('Children Born to Married Couples Over the Years')


plt.subplot(2, 2, 3)
sns.lineplot(data=df, x='Year', y='Divorce Rate', marker='o')
plt.title('Divorce Rate Over the Years')


plt.subplot(2, 2, 4)
sns.lineplot(data=df, x='Year', y='Median Age at First Marriage (Male)', marker='o', label='Male')
sns.lineplot(data=df, x='Year', y='Median Age at First Marriage (Female)', marker='o', label='Female')
plt.title('Median Age at First Marriage')
plt.legend()

plt.tight_layout()
plt.show()

X = df[['Total Marriages']].values.reshape(-1, 1)
y = df['Children Born to Married Couples'].values


regressor = LinearRegression()
regressor.fit(X, y)

# Predict the values
y_pred = regressor.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(df['Total Marriages'], df['Children Born to Married Couples'], color='blue')
plt.plot(df['Total Marriages'], y_pred, color='red', linewidth=2)
plt.title('Regression: Total Marriages vs. Children Born to Married Couples')
plt.xlabel('Total Marriages')
plt.ylabel('Children Born to Married Couples')
plt.show()

print("Regression Coefficient (Slope):", regressor.coef_[0])
print("Regression Intercept:", regressor.intercept_)
print("R-squared:", regressor.score(X, y))
