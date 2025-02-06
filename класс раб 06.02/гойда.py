import pandas as pd


# Чтение Excel-файла
df_excel = pd.read_excel('ZZ1Z.xlsx')

# Посмотреть первые 10 строк
#print(df_excel.head(4))

#print(df_excel.sample(4))

# Посмотреть информацию о таблице
#print(df_excel.info())
n = int(input('ведите ряд'))
m = int(input('введите столбик'))


print("GOYDAA")
print(df_excel.iloc[n,m])

print('lll')
print(df_excel.head(3))
print('ggg')
print(df_excel.sample)
print('hhh')
print(df_excel.tail(5))