#!/usr/bin/python
# -*- coding:utf-8 -*-

#  while 语句
# break 终止循环
# continue 停止执行之后的代码，重新判断循环条件，循环并没有结束
# boolean 0 -- false  1 -- true

current_num = 0
while 1:
    current_num += 1
    if current_num >= 10:
        break
    if current_num % 2 == 0:
        continue
    print(current_num)




