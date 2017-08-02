#!/usr/bin/python
# -*- coding:utf-8 -*-

# if 列表名 ：
#       。。。
# 在列表不为空是返回True

requested_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
#requested_toppings = []
available_toppings = ["mushrooms", "green peppers", "extra cheese"]

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print("Adding  "+requested_topping+". ")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
