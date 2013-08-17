#!/usr/bin/python
#@coding=utf-8
#@Filename: Quiz1.py
#@Author: SR1
#@Date: 2013-08-17

for num in range(0, 20000):
    origin = num*num
    revers = int(''.join((str(origin))[::-1]))
    if revers == origin:
        print origin
