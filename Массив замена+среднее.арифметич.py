"""Підрахувати та вивести на екран
монітору кількість елементів масиву
D(N), значення яких менше
середнього арифметичного усіх
елементів масиву.
Вводим массив и даем ему значения."""
arr = [1 , 2 , 3 , 4 , 5 , 6 , -10, 20, 8, 7 , 8 , 9 , 123 , 134 ]
#Количесвто элементов массива.
L = len(arr)
print('Количество элементов массива=',L)
#Сумма элемеетов массива.
x = (sum(arr))
#Среднее арифметическое.
sum = x/L
print('Сумма элементов массива=',x)
print('Среднее арифметическое',sum)
count = 0
#Мини цикл.
for a in arr:
    if a < sum:
        count += 1
print('Количество элементов, меньше сред.арифметического',count)