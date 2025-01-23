import pandas as pd


df_excel = pd.read_excel('ZZZ.xlsx')

print(df_excel.head(4))

print(df_excel.sample(4))

print(df_excel.info())

print(df_excel.iloc[3])
