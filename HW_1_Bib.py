#!/usr/bin/env python
# coding: utf-8

# #Задание 1 
# Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. Будем считать, что каждый столбец - это признак, а строка - наблюдение. Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. Результат запишите в массив mean_a, в нем должно быть 2 элемента.
# 

# In[4]:


import numpy as np
a = np.array(
    [[1, 2, 3, 3, 1], 
    [6, 8, 11, 10, 7]]
).transpose()
print(a)


# In[5]:


mean_a = np.mean(a, axis = 0)
print(mean_a)


# In[ ]:


# Заданиет 2 
Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, 
содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.


# In[6]:


a_centered = a - mean_a
print(a_centered)


# In[ ]:


# Задание 3 
Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. 
Затем поделите a_centered_sp на N-1, где N - число наблюдений.


# In[7]:


a_centered_sp = a_centered.T[0] @ a_centered.T[1]
print(a_centered_sp)


# In[8]:


a_centered_sp / (a_centered.shape[0] - 1)


# In[ ]:


# Работа с данными Pandas Задание 1
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. 
Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
[1, 1, 1, 2, 2, 3, 3],
['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
[450, 300, 350, 500, 450, 370, 290].


# In[9]:


import pandas as pd
authors = pd.DataFrame({'author_id':[1, 2, 3], 
                        'author_name':['Тургенев', 'Чехов', 'Островский']}, 
                       columns=['author_id', 'author_name'])
print(authors)


# In[10]:


book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3], 
                     'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 
                     'price':[450, 300, 350, 500, 450, 370, 290]}, 
                    columns=['author_id', 'book_title', 'price'])
print(book)


# In[ ]:


# Задание 2 Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.


# In[11]:


authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')
print(authors_price)


# In[ ]:


# Задание 3 Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.


# In[12]:


top5 = authors_price.nlargest(5, 'price')
print(top5)


# In[ ]:


# Задание 4 
Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
author_name, min_price, max_price и mean_price,
в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.


# In[13]:


authors_stat = authors_price['author_name'].value_counts()
print(authors_stat)


# In[14]:


authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})
authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})
print(authors_stat)


# In[ ]:




