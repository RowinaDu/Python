#!/usr/bin/python
# -*- coding:utf-8 -*-

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)

#for magician in magicians:
#print(magician)     #编译报错，不符合缩进规则

for magician in magicians:
    print(magician.title()+",that was a great trick!")
print("I can't wait to see your next trick," + magician.title()+".\n")      #打印一次

for magician in magicians:
    print(magician.title()+",that was a great trick!")
    print("I can't wait to see your next trick," + magician.title()+".\n")  #打印三次




