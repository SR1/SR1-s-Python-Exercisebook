#!/usr/bin/python
#@coding=utf-8
#@Filename: Quiz2.py
#@Author: SR1
#@Date: 2013-08-17

import os
import re

pattern = re.compile(r'\W+')
fin = open('from.txt')
fout = open('to.txt','w')

allword = []
for line in fin:
    allword.extend(pattern.split(line))

allword.sort()
for word in allword:
    if word != '':
        fout.write(word)
        fout.write('\n')
        print word
