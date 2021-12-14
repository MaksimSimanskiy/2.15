#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
В операционных системах на базе Unix обычно присутствует утилита с названием head.
Она выводит первые десять строк содержимого файла, имя которого передается в качестве
аргумента командной строки. Напишите программу на Python, имитирующую поведение
этой утилиты. Если файла, указанного пользователем, не существует, или не задан аргумент командной строки,
необходимо вывести соответствующее сообщение об
ошибке.
"""
import sys
import os.path

if __name__ == "__main__":
    n = int(input("Input count of lines "))
    if n <= 0:
        print("Wrong number")
        exit()
    check = os.path.exists(sys.argv[1])
    if check:
        with open(sys.argv[1], "r") as txt:
            lines = [next(txt) for x in range(n)]
            for line in lines:
                print(line)
    else:
        print("File not exist")
