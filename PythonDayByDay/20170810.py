#!/usr/bin/python
# -*- coding:utf-8 -*-

#删除列表中特定值的所有元素

pets = ["cat", "bird", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")
print(pets)

