#!/usr/bin/python
# -*- coding:utf-8 -*-

# 函数 - 返回值


def get_formatted_name1(first_name, last_name):
    full_name = first_name + "-" + last_name
    return full_name


def get_formatted_name2(first_name, mid_name, last_name):
    if mid_name:
        full_name = first_name + " " + mid_name+" "+last_name
    else:
        full_name = first_name+" "+last_name
    return full_name
musician1 = get_formatted_name1("jimi", "hendrix")
musician2 = get_formatted_name2("jimi", "hooker", "hendrix")
print(musician1)
print(musician2)





