#!/usr/bin/python
# -*- coding:utf-8 -*-
# sort() 排序 ，默认是按照字典序进行排序，字典序暂时理解为AscII码
# a.sort() 对于a进行排序
# sorted(a)返回一个排过序的新的列表
# a.sort(reverse=True) True--降序 False--升序（默认）
# a.revers() 反转
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
print(len(cars))
