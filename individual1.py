#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Написать программу, которая считывает из текстового файла три предложения и выводит их
в обратном порядке.
"""
if __name__ == "__main__":
    list = []
    with open("ind.txt", "r") as txt:
        # running a for loop

        content = txt.readlines()
        content.reverse()
        for line in content:
            print(line)
