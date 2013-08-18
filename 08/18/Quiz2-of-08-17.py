#!/usr/bin/python
#@coding=utf-8
#@Source: http://crossin.me/forum.php?mod=viewthread&tid=534&extra=page%3D1
#@Date: 203-08-18

f = file('from.txt')
data = f.read()
print data
f.close()

def En_check(cha):
    '''这个函数用来判断一个字符是否英文'''
    x = ord(cha) #ord将字符的ASCII或者UNICODE码值返回
    #如果字符是a-zA-Z则返回True，否则返回False
    if x>=97 and x<=122:
        return True
    elif x>=65 and x<=90:
        return True
    return False

def En_split(data):
    '''分离器'''
    En = [] #用于收集所有单词
    En_gather = '' #用于收集单个单词
    flag = True #用于切换
    for cha in data:
        if not flag and En_check(cha):
            flag = True
        elif not En_check(cha) and flag:
            flag = False
            if En_gather != "":
                En.append(En_gather)
        if flag:
            En_gather += cha
        else:
            En_gather = ""
    if En_gather != "":
        En.append(en)
    return En

group = En_split(data)
print data

for word in group:
    print word.decode('utf-8')

group.sort()
print group

for word in group:
    print word.decode('utf-8')

out = open('to.txt','w')
for word in group:
    out.write(word)
    out.write('\n')
out.close()
