#!/usr/bin/python
# -*- coding:utf-8 -*-

#if语句

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
print (car != "bmw")

if car != "bmw":
    print (car.lower())
if ("audi" in cars) and (len(cars) >= 4):
    print("audi in more than 4 cars")
else:
    print("audi not in 4 cars")

