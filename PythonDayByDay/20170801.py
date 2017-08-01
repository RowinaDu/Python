#!/usr/bin/python
# -*- coding:utf-8 -*-

#if语句小案例--根据年龄输出人生阶段 如小于2岁是婴儿

while True:
    age = input("请输入年龄！输入0退出")
    age = int(age)
    if age > 0 and age < 2:
        print(age, "岁是婴儿")
    elif age >=2 and age < 4:
        print(age, "岁正在蹒跚学步")
    elif age >= 4 and age < 13:
        print(age, "岁是儿童")
    elif age >= 13 and age < 20:
        print(age, "岁是青少年")
    elif age >= 20 and age < 65:
        print(age, "岁是成年人")
    elif age >= 65 :
        print(age, "岁是老年人")
    elif age == 0 :
        print("再见")
        break
