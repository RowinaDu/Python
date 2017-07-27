#!/usr/bin/python
# -*- coding:utf-8 -*-

#range() 函数 返回的是一个 range object
#格式 range(i,j,k) 表示从i到j步长为k的列表,含头不含尾
print(range(3))
print(list(range(3, 12, 3)))

#今天的练习
for value in range(6):
    print(value)
print("-------------------\n")

for value in range(1, 5):
    print(value)

print(list(range(4)))
print(list(range(2, 11, 2)))

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

print(max(squares))
print(min(squares))
print(sum(squares))











