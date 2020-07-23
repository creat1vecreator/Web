#!/usr/bin/env python3.4
import os
import sys
import cgi
import cgitb
from random import randint

cgitb.enable()
sys.stderr = sys.stdout
form = cgi.FieldStorage()


def print_form_file(form):
    print('''
\n
<blockquote>
2012. Используя генератор случайных чисел получить одномерный массив числовых значений, насчитывающий А элементов в диапазоне В-С. 
 Определить, образуют ли элементы массива, расположенные перед первым  отрицательным элементом, возрастающую последовательность.
 </blockquote>
<form  action="./lab_1_2_web.py" target="_self" method="get">
<p> 
    
    Enter length of array: <input type="number" name="a" value=26 size=6>
    Enter max number: <input type="number" name="b" value=26 size=6>
    Enter min number: <input type="number" name="c" value=23 size=6>
    Enter the position you want to start deleting from array: 
    <input type="number" name="position" value=10 size=6>
    Enter how many elements you want to delete: 
    <input type="number" name="quantity" value=26 size=6>
   
</p>
<!--Нижерасположенное удалять нельзя, редактировать можно-->
Название файла: <input type="Техт" name="000_file_name" value="g05u90_file.txt" >
Тип записи в файл:<select name="010_mode">
    <OPTION value="a">a - дозаписать в файл(таблицу базы)</OPTION> 
    <OPTION value="w">w - очистить файл(таблицу базы) и записать </OPTION> 
    </select>
<input type="hidden" name="function" value="page">
<input type="hidden" name="page_id" value="8">
<input type="submit" name="submit" value="Отправить">
</form>
    ''')


def form_dictionary(form):
    a = int(form.getvalue('a'))
    b = int(form.getvalue('b'))
    c = int(form.getvalue('c'))
    quantity = int(form.getvalue("quantity"))
    position = int(form.getvalue("quantity"))
    array = []
    for i in range(0, a):
        if c < b:
            array.append(randint(c, b))
        else:
            print('Wrong numbers')
    if position + quantity >= len(array):
        quantity = len(array) - position
    while quantity >= 0:
        del array[position]
        quantity -= 1
    print("<h1>")
    print(array)
    print("</h1>")

    
if __name__ == '__main__':
    print("Content-type:text/html\r\n")
    print('''
        <html>
        <head>
            <title>Лабораторная работа №1</title>
        </head>
        <body> <ul>
                <li>Task 1</li>
                <li><a href="./lab_1_1_web.py" target="_self">Task 1</a></li>
                <li><a href="./lab_1_3_web.py" target="_self">Task 3</a></li>
            </ul>
            <h2>Задание №2</h2>
            <h3>Циферки набрал</h3>
    ''')
    print("\n<pre>")
    print_form_file(form)  # Создаем форму и отправляем данные на сервер
    form_dictionary(form)  # Анализируем строку запроса
    print("\n</pre>")
