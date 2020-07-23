#!/usr/bin/env python3.4
import os
import sys
import cgi
import cgitb
import re

cgitb.enable()
sys.stderr = sys.stdout
form = cgi.FieldStorage()


def form_dictionary(form):
    print("Анализируем строку запроса")
    print("ключи(form.keys):", form.keys())
    form_keys_list = list()
    form_values_list = list()
    form_values_dict = dict()
    print("Названия ключей  и их значения (как есть)")
    i = 0
    for form_key in form.keys():
        print(i, ": ", form_key, " = ", form.getvalue(form_key))
        form_keys_list.append(form_key)
        form_values_list.append(form.getvalue(form_key))
        form_values_dict.update({form_key: form.getvalue(form_key)})
        i += 1
    print('\nВ виде словаря (form_values_dict):\n', form_values_dict)
    # сортируем список ключей (что-бы поля не сбоили при выводе в файл)
    '''print("\n", "Ключи  и их значения после сортировки ")
    form_keys_list.sort()
    i = 0
    for form_key in form_keys_list:
        print(i, ": ", form_key, " = ", form.getvalue(form_key))
        i += 1
    print("form_keys_list: ", form_keys_list)'''
    sum = 0
    for value in form_values_list:
        if re.match('\d+', value):
            sum += int(value)
    print("<h1>", "Your sum: ", sum, "</h1>")
    
    
def file_list(form):
    if "000_file_name" in form:
        file = "../tmp/" + form["000_file_name"].value
        print ("\nЗаписываем в:", file)
        if form["010_mode"].value == 'w':  # 0 - очищаем файл
            file_stream = open(file, mode='w', encoding="utf-8", errors=None)
            file_stream.close()
        file_stream = open(file, mode='a', encoding="utf-8", errors=None)
        form_keys_list = list()
        for form_key in form.keys():
            form_keys_list.append(form_key)
        form_keys_list.sort()
        for form_key in form_keys_list:
            form_value = form.getvalue(form_key)
            file_stream.write("%1s;%1s;" % (form_key, form_value ))
            sys.stdout.write("%1s;%1s;" % (form_key, form_value ))
        file_stream.write("\n")
        file_stream.close()

        listB = list()  # для формирования списка из столбца файла
        r_stream = open(file, mode='r', encoding="utf-8")
        print ("\n\nПострочно считываем строки из ", file, "и разбираем на слова")
        for line in r_stream.readlines():
            print(line, end='')
            words = line.split(";")
            print(words)
            listB.append(int(words[15]))
        print("<h2>")
        print("\nlistB (Список из 16-го столбца файла):", listB)
        print("Длина 16-ого столбца:", listB.__len__())
        print("Сумма: ", sum(listB))
        print("Среднее значение: ", sum(listB) / len(listB))
        print("Максимальное значение: ", max(listB))
        print("Минимальное значение: ", min(listB))
        print("</h2>")






if __name__ == '__main__':
    print("Content-type:text/html\r\n")
    print(
        "<html>\n",
        "<head>\n<title>Подсчёт суммы баллов </title>\n</head>\n",
        "\n<body>\n<h3>Идёт подсчёт суммы баллов</h3>\n<pre>",
    )
    form_dictionary(form)  # Анализируем строку запроса
    file_list(form)
    print("\n</pre>")
    