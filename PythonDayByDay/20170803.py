#!/usr/bin/python
# -*- coding:utf-8 -*-

#Python字典

alien_0 = {}    #声明
print(alien_0)
alien_0 = {"color": "green"}   #添加
print(alien_0["color"])

alien_0["color"] = "red"    #改变value
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
del alien_0["color"] #移除
print(alien_0)
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
    }
print(favorite_languages)
