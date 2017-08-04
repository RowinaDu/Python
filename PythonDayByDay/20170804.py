#!/usr/bin/python
# -*- coding:utf-8 -*-

#Python字典取值（遍历）

user_0 = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}
for key, value in user_0.items():           #如不加items() 会报    ValueError: too many values to unpack (expected 2)
    print("\nkey: " + key)
    print("value: " + value)

for key in user_0.keys():
    print("\nkey: " + key)
    print("value: " + user_0[key])
for value in set(user_0.values()):          #去重value
    print("distinct value: " + value)
print()
for value in user_0.values():
    print("all value: " + value)
