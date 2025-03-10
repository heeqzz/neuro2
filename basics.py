

# или отдельных функций (модулей, объектов и т.п.) из библиотеки
from random import randint

# Выполнение задания №1
spisok=[]#изменил {} на []
sum=0
for i in range(100):
    spisok.append(randint(0,20))#добавил метод append, который вносит в список число.
    if(spisok[i]%2==0):
        sum+=spisok[i]
print(sum)
