import pandas as pd


# Чтение Excel-файла
df_excel = pd.read_excel('ZZZ.xlsx')

# Посмотреть первые 10 строк
print(df_excel.head(4))

print(df_excel.sample(4))

# Посмотреть информацию о таблице
print(df_excel.info())

print(df_excel.iloc[3])
