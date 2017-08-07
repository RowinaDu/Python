#!/usr/bin/python
# -*- coding:utf-8 -*-

#python输入交互--raw_input input
# python2.7中的input() 会将输入的内容运行，可能出现我们不希望的结果，所以使用raw_input()代替
# python3 书写raw_input()会报错,因为他不是内置函数

name = ""
name = input("Please enter your name: ")
print("Hello ", name, " !")

height = input("How tall are yout , in inches ?")
number = int(height)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\The number " + str(number) + " is odd.")

