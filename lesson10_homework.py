# Урок 10 ////////////////////////////////////////////////////////////////////////
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()



import pandas as pd
import random as random

# Создаем DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем новые столбцы для каждой категории и заполняем их нулями
unique_values = data['whoAmI'].unique()
for value in unique_values:
    data[value] = 0

# Устанавливаем соответствующее значение в новых столбцах
for i, row in data.iterrows():
    data.loc[i, row['whoAmI']] = 1

# Выводим первые строки DataFrame
print(data.head())
