#!/usr/bin/python  
# -*-coding:utf-8-*-
import os
import yaml

# dirpath = os.path.dirname(os.path.realpath(__file__))
# f = open("mypage.yaml", "r", encoding="utf-8")
# a = f.read()
# f.close()
# d = yaml.load(a)
# print(d)
# print(d["Mypage"]['desc'])
# for i in d["Mypage"]['locators']:
#     print(i)
dirpath = os.path.dirname(os.path.realpath(__file__))
# print(dirpath)
curpath = os.path.join(dirpath, "mypage.yaml")


def openfile(filename):
    f = open(filename, "r", encoding="utf-8")
    a = f.read()
    f.close()
    d = yaml.load(a)
    return d

a = openfile(curpath)
print(type(a))

def get_locals(page,name):
    alllocal = page['Mypage']['locators']
    for i in alllocal:
        if name == i['name']:
            return i
            # print(i)
            # print(type(i))


c = get_locals(a,"我的")
# print(type(get_locals(a,"我的")))
print(c)