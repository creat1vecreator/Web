#!/usr/bin/env python3.4
import os
import sys
import cgi
import cgitb

cgitb.enable()
sys.stderr = sys.stdout
form = cgi.FieldStorage()


def print_form_file(form):
    print('''
\n
<blockquote>
3012. Вводятся несколько предложений. Вывести в виде строк. Слова в предложении вывести в обратном порядке. Подсчитать слов в каждом предложении.
</blockquote>
<form  action="./lab_1_3_web.py" target="_self" method="get">
<p>
    Enter some string right here:
    <input type="Text" name="str_written" value="Initial parameters. You could put there your own parameters." size=150>
    Enter your string
    <input type="Text" name="string" value="This is the example. You could try by youer own params" size=15>
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
    str_written = form.getvalue('str_written')
    str_formated = str_written.split('.')

    for sentence in str_formated:
        print(sentence.strip(' '))

    str_formated = str_written.split(' ')
    str_res = []

    for word in str_formated:
        if '.' in word:
            word = word[::-1]
            word = word.strip('.') + '.'
            print(word)
            str_res.append(word)
        else:
            word = word[::-1]
            print(word)
            str_res.append(word)

    print("<h1>")
    print(str_res)
    print("</h1>")


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
                <li><a href="./lab_1_1_web.py" target="_self">Task 1</a></li>
                <li><a href="./lab_1_2_web.py" target="_self">Task 2</a></li>
            </ul>
            <h2>Задание №3</h2>
            <h3>Мммм строки мои строки</h3>
    ''')
    print("\n<pre>")
    print_form_file(form)  # Создаем форму и отправляем данные на сервер
    form_dictionary(form)  # Анализируем строку запроса
    print("\n</pre>")
