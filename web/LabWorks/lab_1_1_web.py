#!/usr/bin/env python3.4
import os, sys
import cgi, cgitb

cgitb.enable()
sys.stderr = sys.stdout
form = cgi.FieldStorage()


def print_form_file(form):
    print('''
\n
<blockquote>
1012. Даны вещественные числа: A, B, C. Определить, выполняются ли неравенства 
A < B < C или A > B > C и какое именно неравенство выполняется.
<form  action="./lab_1_1_web.py" target="_self" method="get">
</blockquote>
<p>
    Enter three Variables A, B, C: 
    A: <input type="number" name="A" value= 0 size=4>
    B: <input type="number" name="B" value= 1 size=4>
    C: <input type="number" name="C" value= 2 size=4>
    

</p>
<!--Нижерасположенное удалять нельзя, редактировать можно-->
Название файла: <input type="Техт" name="000_file_name" value="g05u94_file.txt" >
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
    a = int(form.getvalue("A"))
    b = int(form.getvalue('B'))
    c = int(form.getvalue('C'))
    if a < b < c:
        print("Выполняется неравенство:  A < B < C")
    elif a > b > c:
        print("Выполняется неравенство:  A > B > C")
    else:
        print("Невыполнется никакое из неравенств")


if __name__ == '__main__':
    print("Content-type:text/html\r\n")
    print('''
        <html>
        <head>
            <title>Лабораторная работа №1</title>
        </head>
        <body>
             <ul>
                <li>Task 1</li>
                <li><a href="./lab_1_2_web.py" target="_self">Task 2</a></li>
                <li><a href="./lab_1_3_web.py" target="_self">Task 3</a></li>
            </ul>
            <h2>Задание №1</h2>
            <h3>Неравенства</h3>
    ''')
    print("\n<pre>")
    print_form_file(form)  # Создаем форму и отправляем данные на сервер
    form_dictionary(form)  # Анализируем строку запроса
    print("\n</pre>")
