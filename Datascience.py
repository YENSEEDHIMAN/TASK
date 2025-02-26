import pandas as pd


url='/home/yensee/Desktop/TASK_S/data.csv'
df=pd.read_csv(url)
# print(df.to_string())
# print(df.tail())
# print(df.head())
# print(df.info())
# print(df.describe())
print(df['hindi'].describe())
print(df['hindi'].count())

# Mean (Average)
print(df['hindi'].mean())

# Median
print(df['hindi'].median())

# Mode (Most frequent value)
print(df['hindi'].mode())

# Standard Deviation (Measure of spread)
print(df['hindi'].std())

# Variance (Measure of dispersion)
print(df['hindi'].var())

print(df['hindi'].value_counts())

# Percentage distribution
print(df['hindi'].value_counts(normalize=True) * 100)
# print(df.isnull().sum())
# df = df.drop_duplicates()
# print(df.duplicated().sum())
# df = df.dropna()
# print(df.to_string())
# df = pd.get_dummies(df, columns=['punjabi'], drop_first=True)
# df['hindi'] = pd.to_numeric(df['hindi'])
# print(df.to_string())

