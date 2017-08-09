#!/usr/bin/python
# -*- coding:utf-8 -*-

#列表之间移动元素

unconfirmed_user = ["Rose", "Lucy", "Jack"]
confirmed_user = []

while unconfirmed_user:
    confirmed_user.append(unconfirmed_user.pop())
print("All user has been confirmed,They all in confirmed_user: ", confirmed_user)
print("The unconfirmed_user was empty:", unconfirmed_user, "cause remove")




