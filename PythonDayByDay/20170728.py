#!/usr/bin/python
# -*- coding:utf-8 -*-

players = ["charles", "martina", "michael", "florence", "eli"]
#--------------0----------1----------2----------3---------4---
#==============-5=========-4=========-3=========-2========-1==
#[i:j]表示从第i个开始截取到j,含头不含尾，负数表示从后往前计
print(players[0:3])
print(players[ :4])
print(players[ :-1])
print(players[ :-3])
print(players[-1: ])
print(players[-3: ])

for player in players[0:3]:
    print(player.title())

c_players = players[ : ]
c_players.pop()
print("clone:", c_players)
print("orgin:", players)

p_players = players #此处指向同一个地址
p_players = p_players.pop()
print("orgin:", players)
